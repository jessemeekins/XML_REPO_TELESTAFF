#%%  
FIRST_RESPONERS_COMPANIES = {
        "BC001" : {
            "FIRE":['PU001', 'PU002', 'PU005', 'PU007','TR13', 'PU008','TR005'],
            "UNITS":[]
        },
        "BC002" : {
            "FIRE":['PU004', 'TR002', 'PU015', 'PU019', 'PU026', 'TR011', 'PU028'],
            "UNITS":[]
        },
        "BC003" : {
            "FIRE":['PU010', 'TR021', 'PU014', 'PU020', 'PU029', 'RC002', 'PU032'],
            "UNITS":[]   
        },
        "BC004" : {
            "FIRE":['QT054', 'PU056', 'PU058', 'TR030', 'PU059'],
            "UNITS":[]   
        },
        "BC005" : {
            "FIRE":['PU017', 'TR008', 'PU023', 'PU024', 'QT048', 'PU051', 'TR010'],
            "UNITS":[]  
        },
        "BC006" : {
            "FIRE":['PU011', 'TR004', 'PU013', 'PU016', 'PU018', 'PU022', 'TR007' ],
            "UNITS":[]  
        },
        "BC007" : {
            "FIRE":['PU021', 'TR015', 'PU025', 'RC001', 'PU030', 'PU041', 'TR020', 'PU044'],
            "UNITS":[]
        },
        "BC008" : {
            "FIRE":['PU034', 'PU040', 'PU042', 'PU050', 'TR021', 'QT057'],
            "UNITS":[]
        },
        "BC009" : {
            "FIRE":['PU036', 'TR019', 'QT037', 'PU38', 'TR024', 'PU039', 'TR018', 'PU043', 'PU045' ],
            "UNITS":[]
        },
        "BC010" : {
            "FIRE":['PU035', 'TR017', 'PU052', 'PU053', 'PU055', 'TR027'],
            "UNITS":[] 
        },
        "BC011" : {
            "FIRE":['PU027', 'RC003', 'PU031', 'PU046', 'PU047', 'TR023'],
            "UNITS":[]
        }
    }


FIRST_DIVISION = {}
SECOND_DIVISION = {}

for k,v  in FIRST_RESPONERS_COMPANIES.items():
    query = v['FIRE']
    if "PU025" in query:
        print(k, query)
#%%

item=FIRST_RESPONERS_COMPANIES.get("BC007", None)
print(item)