import xml.dom.minidom
import __main__

class xmlserialize(object): pass
class xmlunpicklingException(Exception): pass
	
class xmlfile(object):
	""" Class to handle saving / loading an xmlserialize object to file """
	def __init__(self, filename=None):
		self.filename = filename
		
	def load(self):
		''' Load xml from self.filename, return object '''
		node = xml.dom.minidom.parse(self.filename)
		return self.unpickle(node.documentElement)
		
	def save(self, obj):
		''' Save node to self.filename '''
		node = self.pickle(root=obj, fabric=xml.dom.minidom.Document())
		f = open(self.filename, 'w')
		node.writexml(f)
		f.close()
		
	# helper functions
	def getMod(self, cls):
		'''
		cls would be in the form like module1.module2.cls
		Loops through __main__ to see how module1.module2 is imported
		Returns the class(obj) using the existing import method
		Returns None if the module or class isn't found
		'''
		import __main__
		# separate the module from the class [module1.module2].[cls]
		print "Class: %s" % cls
		mod = cls[0:cls.rindex('.')]
		className = cls[cls.rindex('.')+1:]
	
		for d in dir(__main__):
			try:
				m = eval('__main__.%s.__name__' % d)
				if cls == (m + "." + className):
					return eval('__main__.%s.%s()' % (d,className ))
			except:
				pass # Ignore if no attribute __name__
		
		return None
	
	def getType(self, obj):
		""" Generates string representation of class of obj 
			discarding decoration """
		#return str(obj.__class__).split("'")[1].split(".")[-1]
		return str(obj.__class__).split("'")[1]
		
	_easyToPickle = [ "int", "float", "str" ]
	
	def _isCallable(self, obj):
		return hasattr(obj, "__call__")
	
	# 
	#   pickling 
	# 
	
	def _pickleDictItems(self, root, node, fabric):
		for key, value in root.items():
			tempnode = fabric.createElement("item")
			tempnode.appendChild(self.pickle(key, fabric, "key"))
			tempnode.appendChild(self.pickle(value, fabric, "value"))
			node.appendChild(tempnode)
	
	def _pickleListItems(self, root, node, fabric):
		for idx, obj in enumerate(root):
			tempnode = self.pickle(obj, fabric, "item")
			tempnode.attributes["index"] = str(idx)
			node.appendChild(tempnode)
		
	_pickleTupleItems = _pickleListItems
	
	def pickle(self, root, fabric, elementName="root"):
	
		node = fabric.createElement(elementName)
		typeStr = self.getType(root)
		node.attributes["type"]=typeStr
		
		if isinstance(root, xmlserialize):
			node = self._pickleObjectWithAttributes(node, root, fabric, elementName)
		elif typeStr in self._easyToPickle:
			node.appendChild(fabric.createTextNode(str(root)))
		elif isinstance(root, dict):
			self._pickleDictItems(root, node, fabric)
		elif isinstance(root, list):
			self._pickleListItems(root, node, fabric)
		elif isinstance(root, tuple):
			self._pickleTupleItems(root, node, fabric)
		else:
			# fallback handler
			node.appendChild(fabric.createTextNode(repr(root)))
		return node
	
	def _pickleObjectWithAttributes(self, node, root, fabric, elementName):
		''' Pickle all members or just a subset ??? '''
		if hasattr(root, "__pickle_to_xml__"):
			attributesToPickle = root.__pickle_to_xml__
		else:
			# avoid members which are python internal
			attributesToPickle = [ name for name in dir(root) if not name.startswith("__") ]
		
		for name in attributesToPickle:
			obj = getattr(root, name)

			# do not pickle member functions
			if self._isCallable(obj): continue
		
			# is there some special encoding method ??
			if hasattr(root, "_xml_encode_%s" % name):
				value = getattr(root, "_xml_encode_%s" % name)()
				element = fabric.createElement(name)
				element.attributes["type"]='custom'
				element.appendChild(fabric.createTextNode(value))
				node.appendChild(element)
			else:
				node.appendChild(self.pickle(obj, fabric, name))
		return node
	
	#
	#   unpickling 
	#
	
	# helper functions
	
	def _getElementChilds(self, node, doLower = 1):
		""" returns list of (tagname, element) for all element childs of node """
		
		dolow = doLower and (lambda x:x.lower()) or (lambda x:x)
		return [ (dolow(no.tagName), no) for no in node.childNodes if no.nodeType != no.TEXT_NODE ]
	
	def _getText(self, nodelist):
		""" returns collected and stripped text of textnodes among nodes in nodelist """
		rc = ""
		for node in nodelist:
			if node.nodeType == node.TEXT_NODE:
				rc = rc + node.data
		return rc.strip()
	

	def unpickle(self, node, obj=None):
		''' main unpickle function '''
		typeName= node.attributes["type"].value
		
		if typeName in self._easyToPickle: 
			initValue = self._getText(node.childNodes)
			return eval("%s(%r)" % (typeName, initValue))
		elif typeName=="tuple":
			return self._unpickleTuple(node)
		elif typeName=="list":
			return self._unpickleList(node)
		elif typeName=="dict":
			return self._unpickleDict(node)
		elif typeName=="custom":
			fun = "_xml_decode_%s" % node.tagName
			if not obj or not fun in dir(obj) : return ''
			return eval("__main__.%s.%s('%s')" % (self.getType(obj), fun, self._getText(node.childNodes)))
		else:
			try:
				obj = eval("__main__.%s()" % typeName)
			except:
				obj = self.getMod(typeName)
			
			for name, element in self._getElementChilds(node):
				obj.__dict__[name] = self.unpickle(element, obj)
			return obj
	
	def _unpickleList(self, node):
		li = []
		# collect entries, you can not assume that the
		# members of the list appear in the right order !
		for name, element in self._getElementChilds(node):
			if name != "item":
				raise xmlunpicklingException()
			idx = int(element.attributes["index"].value)
			obj = self.unpickle(element)
			li.append((idx, obj))
		
		# rebuild list with right order
		li.sort()
		return [ item[1] for item in li ]
	
	def _unpickleTuple(self, node):
		return tuple(self._unpickleList(node))
	
	def _unpickleDict(self, node):
		dd = dict()
		for name, element in self._getElementChilds(node):
			if name != "item":
				raise xmlunpicklingException()
			childList = self._getElementChilds(element)
			if len(childList) != 2:
				raise xmlunpicklingException()
			for name, element in childList:
				if name=="key":
					key = self.unpickle(element)
				elif name=="value":
					value = self.unpickle(element)
			dd[key]=value
		return dd