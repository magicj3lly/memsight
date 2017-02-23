
def start():
	return 0x400526

def end():
	return [0x40055d]

def avoid():
	return [0x400576, 0x400577]

def do_start(state):
	params = {}
	params['esi'] = state.regs.esi
	params['edi'] = state.regs.edi
	#state.memory.store(0x601040, 0x0, 4)
	#state.memory.store(0x601044, 0x0, 4)
	return params

def do_end(state, params):

	o = state.se.Concat(params['edi'], params['esi'])
	sol = state.se.any_n_int(o, 5)
	import ctypes
	esi = []
	edi = []
	for k in range(len(sol)):
		edi.append(ctypes.c_int((sol[k] & (0xFFFFFFFF << 32)) >> 32).value)
		esi.append(ctypes.c_int(sol[k] & 0xFFFFFFFF).value)
		assert edi[-1] == esi[-1]

	print "EDI: " + str(edi)
	print "ESI: " + str(esi)
