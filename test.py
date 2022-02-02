import hivemcapi

def swar_test():
    uuid = hivemcapi.swars.player("Twiggylogan6765")
    assert uuid == uuid["UUID"]
    
def twar_test():
    uuid = hivemcapi.twars.player("Twiggylogan6765")
    assert uuid == uuid["UUID"]

def sg_test():
    uuid = hivemcapi.sg.player("Twiggylogan6765")
    assert uuid == uuid["UUID"]

def murder_test():
    uuid = hivemcapi.murder.player("Twiggylogan6765")
    assert uuid == uuid["UUID"]

def hideseek_test():
    uuid = hivemcapi.hideseek.player("Twiggylogan6765")
    assert uuid == uuid["UUID"]

def swar_test():
    uuid = hivemcapi.deathrun.player("Twiggylogan6765")
    assert uuid == uuid["UUID"]