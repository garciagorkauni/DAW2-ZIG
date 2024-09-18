def batu(num1, num2):
    try:
        return int(num1) + int(num2)
    except ValueError:
        return 'Akatsa: datu mota baliogabea'
    except:
        return 'Akatsa'
    
def kendu(num1, num2):
    try:
        return int(num1) - int(num2)
    except ValueError:
        return 'Akatsa: datu mota baliogabea'
    except:
        return 'Akatsa'
    
def bidertu(num1, num2):
    try:
        return int(num1) * int(num2)
    except ValueError:
        return 'Akatsa: datu mota baliogabea'
    except:
        return 'Akatsa'

def zatitu(num1, num2):
    try:
        return int(num1) / int(num2)
    except ValueError:
        return 'Akatsa: datu mota baliogabea'
    except ZeroDivisionError:
        return 'Akatsa: Zenbakia ezin da zeroz zatitu'
    except:
        return 'Akatsa'