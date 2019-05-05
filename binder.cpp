#include <python3.7m/Python.h>
#include "csv.h"
#include <string>
#include <stdexcept>
#include <vector>

std::string module = "csvcpp";


PyObject * vectorToList(std::vector<std::string> &data){

	PyObject * list = PyList_New(data.size());
	if (list==NULL){return NULL;}
	PyObject * dat;
	for (int i = 0; i < data.size(); i++){
		dat = PyUnicode_FromString(data[i].c_str());
		if (dat==NULL){return NULL;}
		PyList_SET_ITEM(list, i, dat);
	}
	return list;
	
}

typedef std::vector<std::vector<std::string>> vvstr;

PyObject * vectorVectorToList(vvstr data){
	PyObject * list = PyList_New(data.size());
	if (list==NULL){return NULL;}
	PyObject * dat;
	for (int i = 0; i < data.size(); i++){
		dat = vectorToList(data[i]);
		if (dat==NULL){return NULL;}
		PyList_SET_ITEM(list, i, dat);

	}
	return list;	
}

PyObject * listCsvRead(PyObject * self, PyObject * args){
	//printf("0\n");
	char *fileName;
	//printf("1\n");
	if (!PyArg_ParseTuple(args, "s", &fileName)){
		return NULL; ("listCsvRead(): wrong argument type\n");
	}
	//printf("2\n");
	//printf("%s\n", fileName);
	FILE * fp = fopen(fileName, "r");
	//printf("3\n");
	CSV csv = CSV(fp);
	//printf("4\n");
	return vectorVectorToList(csv.csv_data_vector);
}

PyMethodDef csvcpp_funcs[] = {
	{"listCsvRead", (PyCFunction)listCsvRead, METH_VARARGS, "listCsvRead(csvFileName): Read CSV and return list"},
	{NULL, NULL, 0, NULL}
};

char module_doc[] = "CSV Reader from C++ core";

PyModuleDef csvcpp_module = {
	PyModuleDef_HEAD_INIT,
	module.c_str(),
	module_doc,
	-1,
	csvcpp_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_csvcpp(void){
	return PyModule_Create(&csvcpp_module);
}

// int main(){
// 	FILE * fp = fopen("diabetes.csv", "r");
// 	//printf("3\n");
// 	CSV csv = CSV(fp);
// 	return 0;
// }
