#Python3
#what I Know

Tasks:
	-read/extract:
		-sources: 
			-HTML
			-XML
			-XLSX
			-JSON:
				-pandas.read_json(file,..)
				-json.loads(filename.read())
			-CSV
			-(Raw) Text (iterator based)
			-XML
			-web
			-csv_reader( iterator based):
				-read_csv_alternative.py 
	-write/store:
		-XMLcd
		-JSON
		-mongodb
		-sql_alchemy:
			-postgresql
			-SQLite
	-typecast:
		-string_to_integer	: int(x) 
		-integer_to_string	: str(X)
		-float_to_integer	: 
		-integer_to_float	: 
		-integer_to_datetime	:  pd.to_datetime(x,infer_datetime_format=True)
		-string_to_datetime	: 
		-datetime_to_integer	:  
		-datetime_to_string	: 
	-dataframe_create:
		-from list(s):
		-from dict(s): pd.DataFrame({'year': [2015, 2016],
                       'month': [2, 3],
                       'day': [4, 5]})
		-from tuple(s):
		-
	-function_timer:
		-jupyter:
			- %timeit: %timeit pd.to_datetime(20173828)
	-Function_tools:
		-mapuseful_functions:
			-np.array_equal(arr1,arr2)
		-reduce
		-apply
		-lambda
		-list_comprehensions
		-zip of lists:
			-a = zip(x,y,z) #len(a) = min(len(x), len(y), len(z))




unstable:
	useful_functions:
		-np.array_equal(arr1,arr2)
		-np.column_stack((X, y))
		-np.random.binomial(n, p, size=None)
		-arr.astype(bool)
		-fit_transform(X, y=None, **fit_params) >--> X_new : numpy array of shape [n_samples, n_features_new]
		-pd.DataFrame.fillna(self, value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)


Question:
Q1:
with open(...) as s
VERSUS
s = open(...)