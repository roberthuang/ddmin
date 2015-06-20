import sys,outputters
from split import split
from xml.parsers.xmlproc import xmlval,xmlproc
from listsets import listminus

PASS       = "PASS"
FAIL       = "FAIL"
UNRESOLVED = "UNRESOLVED"
MAX_DEGREE = 5

def ddmin(data, test,n=1):
	"""Return a sublist of CIRCUMSTANCES that is a relevant configuration
       	   with respect to TEST."""
	subsets=split(data,n)
	for subset in subsets:	
		if test(subset)==FAIL:
			return ddmin(subset,test,2)
		else:
			continue

           
	

	
  
    
    



if __name__ == "__main__":
	tests = {}
	warnings=1
    	entstack=0
    	rawxml=0
	
	
    	fname = sys.argv[1]
    	file1 = open(fname, 'r')
    	data = file1.read()
    	file1.close() 
	
	app = xmlproc.Application()
    	p = xmlproc.XMLProcessor()  
    	p.set_application(app)
    	err=outputters.MyErrorHandler(p, p, warnings, entstack, rawxml)
    	p.set_error_handler(err)






	def getfile(s):
		temp=open('temp.xml','w+')
		 
		temp.write(s)
		temp.flush()
		temp.close()
		return temp.name

	def tempfile():
		temp=open('temp.xml','r')
		data=temp.read()
		temp.close()
		return data

	def test(c):
		
		global tests
		s= ""
		for char in c:
            		s += char

        	if s in tests.keys():
            		return tests[s]
		
		try:
			p.set_data_after_wf_error(0)
            		p.parse_resource(getfile(c))
			
            	except SyntaxError:
                	
                	tests[s] = UNRESOLVED
                	return UNRESOLVED
		except UnboundLocalError:
            		print FAIL   
            		tests[s] = FAIL
            		return FAIL
		else :
                	
                	tests[s] = PASS
                	return PASS
													
	
	ddmin(data,test)
	
	












    

   
