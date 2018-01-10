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