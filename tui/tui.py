
# python wrapper for package wordspace/gosrc/tui within overall package tui
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=./tui ./gosrc/tui/

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _tui
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from tui import tui
# and then refer to everything using tui. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for slice []*tui.Word
class Slice_Ptr_tui_Word(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.Slice_Ptr_tui_Word_CTor()
			_tui.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_Ptr_tui_Word.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		s = 'tui.Slice_Ptr_tui_Word len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'tui.Slice_Ptr_tui_Word([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _tui.Slice_Ptr_tui_Word_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _tui.Slice_Ptr_tui_Word_len(self.handle)
				return Slice_Ptr_tui_Word(handle=_tui.Slice_Ptr_tui_Word_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return Word(handle=_tui.Slice_Ptr_tui_Word_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_tui.Slice_Ptr_tui_Word_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_Ptr_tui_Word.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = Word(handle=_tui.Slice_Ptr_tui_Word_elem(self.handle, self.index))
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_tui.Slice_Ptr_tui_Word_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct tui.ResultSet
class ResultSet(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_ResultSet_CTor()
			_tui.IncRef(self.handle)
			if  0 < len(args):
				self.WordOfInterest = args[0]
			if "WordOfInterest" in kwargs:
				self.WordOfInterest = kwargs["WordOfInterest"]
			if  1 < len(args):
				self.VectorDim = args[1]
			if "VectorDim" in kwargs:
				self.VectorDim = kwargs["VectorDim"]
			if  2 < len(args):
				self.SimilarWords = args[2]
			if "SimilarWords" in kwargs:
				self.SimilarWords = kwargs["SimilarWords"]
			if  3 < len(args):
				self.Distances = args[3]
			if "Distances" in kwargs:
				self.Distances = kwargs["Distances"]
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.ResultSet{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.ResultSet ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def WordOfInterest(self):
		return Word(handle=_tui.tui_ResultSet_WordOfInterest_Get(self.handle))
	@WordOfInterest.setter
	def WordOfInterest(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_ResultSet_WordOfInterest_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def VectorDim(self):
		return _tui.tui_ResultSet_VectorDim_Get(self.handle)
	@VectorDim.setter
	def VectorDim(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_ResultSet_VectorDim_Set(self.handle, value.handle)
		else:
			_tui.tui_ResultSet_VectorDim_Set(self.handle, value)
	@property
	def SimilarWords(self):
		return Slice_Ptr_tui_Word(handle=_tui.tui_ResultSet_SimilarWords_Get(self.handle))
	@SimilarWords.setter
	def SimilarWords(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_ResultSet_SimilarWords_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Distances(self):
		return go.Slice_float32(handle=_tui.tui_ResultSet_Distances_Get(self.handle))
	@Distances.setter
	def Distances(self, value):
		if isinstance(value, go.GoClass):
			_tui.tui_ResultSet_Distances_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))

# Python type for struct tui.Word
class Word(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_tui.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_tui.IncRef(self.handle)
		else:
			self.handle = _tui.tui_Word_CTor()
			_tui.IncRef(self.handle)
	def __del__(self):
		_tui.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Word{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'tui.Word ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def Plot(words):
	"""Plot([]object words) str"""
	return _tui.tui_Plot(words.handle)
def Visualize(centralWord, centralWordVec, closestWords, closestWordDistances, closestWordVectors):
	"""Visualize(str centralWord, []float centralWordVec, []str closestWords, []float closestWordDistances, []float closestWordVectors) str"""
	return _tui.tui_Visualize(centralWord, centralWordVec.handle, closestWords.handle, closestWordDistances.handle, closestWordVectors.handle)


