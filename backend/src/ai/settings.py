"""
    The global varabiles
"""

"""
The list of models names
"""
MODELS_NAMES = [
    'Patient',
    'PrimaryDiagnose',
    'TakingMedicine',
    'Complaint',
    'BloodAnalysis',
    'Other'
]

# The DISCRIPTION_FEATURES is that taking the featureas when is computing from all features
# It is alsa array with in nested dictionary
"""
Keys discription
'feature' : 'birthday', # That key must be the same with features in the models
'display' : 'Birthday', # That key must be title of the feature, it is filled by localization function
'type' : 'date', # that key must be type of the feature
'is_computing': True, # label of the feature to make the feature is taking on computing.
'is_display': True, # label of the feature to make the feature is displaying always. When is_computing is true, 
        then it is not nessecary to set on it True
'is_id': False, # # label of the feature to make the feature is id of some nested feature
Comment: we must to refactor type by python coding
And it is filled with other initial attributs in AIConfig class.
"""
DISCRIPTION_FEATURES = {
    # The features in Patient model
    'Patient': [
        {
            'feature': 'number',
            'type': 'int',
            'is_computing': False,
            'is_display': True,
            'is_id': False,
        },
        {
            'feature': 'last_name',
            'type': 'str',
            'is_computing': False,
            'is_display': True,
            'is_id': False,
        },
        {
            'feature': 'first_name',
            'type': 'str',
            'is_computing': False,
            'is_display': True,
            'is_id': False,
        },
        {
            'feature': 'middle_name',
            'type': 'str',
            'is_computing': False,
            'is_display': True,
            'is_id': False,
        },
        {
            'feature': 'address',
            'type': 'str',
            'is_computing': False,
            'is_display': True,
            'is_id': False,
        },
        {
            'feature': 'status',
            'type': 'bool',
            'is_computing': False,
            'is_display': True,
            'is_id': False,
        },
        {
            'feature': 'birthday',
            'type': 'date',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'fromdate',
            'type': 'date',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            # District id, if it must be take exact name of district we can use API
            'feature': 'district',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': True,
        },
        {
            'feature': 'gender',  # Gender code true-male, false - female
            'display': 'Gender',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'occupation',  # Occution id
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': True,
        },
    ],

    # The next features in PrimaryDiagnose model
    'PrimaryDiagnose': [
        {
            'feature': 'clinicalform',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': True,
        },
        {
            'feature': 'localization',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': True,
        },
        {
            'feature': 'prevalence',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': True,
        },
        {
            'feature': 'infiltration',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'decay',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'seeding',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'resorption',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'compaction',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'scarring',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'calcification',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'bk',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        }
    ],
    # The next features in TakingMedicine model
    'TakingMedicine': [
        {
            'feature': 'patient',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': True,
        },
        {
            'feature': 'fromdate',
            'type': 'date',
            'is_computing': False,
            'is_display': True,
            'is_id': False,
        },
        {
            'feature': 'streptomycin',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'rifampicin',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'isoniazid',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'pyrazinamide',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'ethambutol',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'status',
            'type': 'bool',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'date',
            'type': 'date',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        }
    ],
    # The next features in Complaint model
    'Complaint': [
        {
            'feature': 'patient',
            'type': 'int',
            'is_computing': False,
            'is_display': True,
            'is_id': True,
        },
        {
            'feature': 'diarrhea',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'normal_stool',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'constipation',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'flatulence',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'stomachache',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'from_stool_frequency',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'to_stool_frequency',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'character',
            'type': 'int',
            'is_computing': True,
            'is_display': False,
            'is_id': True,
        },
        {
            'feature': 'status',
            'type': 'bool',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'date',
            'type': 'date',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        }
    ],
    # The next features in BloodAnalysis model
    'BloodAnalysis': [
        {
            'feature': 'patient',
            'type': 'int',
            'is_computing': False,
            'is_display': True,
            'is_id': True,
        },
        {
            'feature': 'er',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'leyk',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'hb',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'color',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'pya',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'sya',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'eoz',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'lf',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'mon',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'coe',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'act',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'alt',
            'type': 'float',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'status',
            'type': 'bool',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'date',
            'type': 'date',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        }
    ],
    # The next features in Other model
    'Other': [
        {
            'feature': 'patient',
            'type': 'int',
            'is_computing': False,
            'is_display': True,
            'is_id': True,
        },
        {
            'feature': 'tuberculosis_tolerance',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'related_disease',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'nausea',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'vomiting',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'headache',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'sweating',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'weakness',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'allergodermatosis',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'from_weight_loss',
            'type': 'float',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'to_weight_loss',
            'type': 'float',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'coproscopy',
            'type': 'bool',
            'is_computing': True,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'status',
            'type': 'bool',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        },
        {
            'feature': 'date',
            'type': 'date',
            'is_computing': False,
            'is_display': False,
            'is_id': False,
        }
    ]
}