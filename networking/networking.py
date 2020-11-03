#!/usr/bin/env python3
#sudo apt install python3-pip
#python3 -m pip install pyexcel
#python3 -m pip install pyexcel-xls
#import pyexcel
#import ansible
# Define the path of configuration file stored in excel format
excel_path = os.path.join(os.getcwd(), r'Excel_folder\configurations\config.xlsx')

# Capture Node A and Node B columns
columns_A = ['Node A Name', 'Node A Interface', 'Node A Description', 'Node A VRF', 'Node A IP', 'Node A Mask']
columns_B = ['Node B Name', 'Node B Interface', 'Node B Description', 'Node B VRF', 'Node B IP', 'Node B Mask']

# import excel file as Pandas Dataframe then split it into two smaller Dataframe
df_int = pd.read_excel(excel_path, sheet_name='P2P')
df_NodeA = pd.DataFrame(df_int, columns = columns_A)
df_NodeB = pd.DataFrame(df_int, columns = columns_B)

# convert nodeA and nodeB config into list of dict format
df_listA = df_NodeA.to_dict('records')
df_listB = df_NodeB.to_dict('records')

