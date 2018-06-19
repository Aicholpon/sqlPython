class crazyclass ():
    
    def find_companies_related_to_companies_via_founders(companies, db_connection=conn):
    frames = []
    for company in companies:
        frames.append(find_companies_by_name(company, db_connection))
    df = pd.concat(frames) # TODO remove duplicates
    return find_related_companies_by_founders(df, db_connection)
    
def find_related_companies_by_founders(companies_dataframe, db_connection=conn):
    companies_array = companies_dataframe.values
    companies_list = list(map(find_companies_by_founders_string, companies_array))
    data = {}
    for i, company in enumerate(companies_array):
        data[company[0]] = companies_list[i]
    return data

def find_companies_by_founders_string(company_with_founders, db_connection=conn):
    founders_list = company_with_founders[1].split(',')
    #companies_list = list(map(find_companies_by_founder, founders_list))
    data = {}
    for i, founder in enumerate(founders_list):
        data[founder] = find_companies_by_founder(founder, company_with_founders[0], db_connection)
    return data

def find_companies_by_founder(founder, nosearch, db_connection=conn):
    df = pd.read_sql_query(
    "SELECT FullNameRu FROM Minjust2018 WHERE Founders LIKE '%"+ founder +"%' AND FullNameRu <> '"+nosearch+"' LIMIT 0, 10",
    db_connection)
    return df.values.tolist()

def find_companies_by_name(name, db_connection=conn):
    df = pd.read_sql_query(
    "SELECT FullNameRu, Founders FROM Minjust2018 WHERE FullNameRu LIKE '%"+name+"%' LIMIT 0, 20",
    db_connection)
    return df





