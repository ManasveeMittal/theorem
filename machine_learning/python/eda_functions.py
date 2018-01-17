#DATA OVERVIEW
def overview(data,first_n_cols = None,log_file=False):
    """ save/display data summary  """

    attributes = data.columns
    if first_n_cols != None:
        data = data[attributes[:first_n_cols]]
    print('\n feature : shape '+ str(data.shape))
    print('\n feature : first_n_rows '+ str(data.head()))
    print('\n feature : attributes ' + str(attributes))
    print('\n feature : data_description ' + str(data.describe()))
#     print('\n feature : data_information ' ,data.info)
    print('\n feature : overview end')






# df = pd.read_csv(f0,sep = ';')
# t = pd.DataFrame(df.columns,columns=['col_name'])

# def col_summary(col_name,df, p1 = ''): This is what i want to do
def col_summary(col_name): #this i am doing currently
    """summarise all cols"""
  	from pandas.api.types import is_numeric_dtype, is_string_dtype
    col = df[col_name]
    TotalRows = len(df)
    TotalUniqueLevels = col.nunique()
    PercentUniqueValues = TotalUniqueLevels/TotalRows
    TotalNullValues = col.isnull().sum()
    PercentNullValues = TotalNullValues/TotalRows
    IdColFlag = TotalRows==TotalUniqueLevels
    # DataType = columntype(col)
    DataType = 'yettobedefined'
    UniqueValue = col.value_counts().to_dict() if TotalUniqueLevels <= 10 else {}
    mean = round(col.mean(),2) if DataType == 'numeric' else None
    min = round(col.min(),2) if DataType == 'numeric' else None
    q1 = round(col.quantile(q=0.25),2) if DataType == 'numeric' else None
    median = round(col.median(),2) if DataType == 'numeric' else None
    q3 = round(col.quantile(q=0.75),2) if DataType == 'numeric' else None
    max = round(col.max(),2) if DataType == 'numeric' else None
    null_flag = col.isnull().all()
    constant_flag = TotalUniqueLevels==1
    output = [TotalRows,TotalUniqueLevels,PercentUniqueValues,TotalNullValues, PercentNullValues,IdColFlag,\
              DataType,UniqueValue,min,q1,mean,median,q3,max,null_flag,constant_flag]
    return output

# defining all these cols look undity, how to improve?, to dict maybe?
# t['TotalRows'],t['TotalUniqueLevels'],t['PercentUniqueValues'],t['TotalNullValues'],t['PercentNullValues']\
# ,t['IdColFlag'],t['DataType'],t['UniqueValue'],t['Min'],t['Q1'],t['Mean'],t['Median'],t['Q3'],t['Max']\
# ,t['Null_flag'],t['Constant_flag'] = zip(*t['col_name'].map(col_summary))  #pass multiple params to map
# print(t)



def get_unique_count(x):
    return len(np.unique(x))