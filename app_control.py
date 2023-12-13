import streamlit as st

def app_locations():
    return {
        'project_data' : 'data/ctm_internal_boonville.csv',
        }

def apply_custom_css():
    default = """
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;} 
        header {visibility: hidden;}
        h1 {color: #593773cc; text-align:left; padding: 0px 0px 1rem 0px; text-shadow: 0 3px 3px rgba(0,0,0,0.2); font-weight: 100;}
        h2 {color: #593773; padding: 1rem 0px 0px 0px; font-weight:300;}
        h3 {color: #593773cc; padding: 0px 0px 1rem 0px; text-shadow: 0 3px 3px rgba(0,0,0,0.2); font-weight: 100;}
        a {color: #593773; text-decoration: none;}
        .stTextArea {box-shadow: 2px 3px 1px rgba(0,0,0,0.2);}
        .stTextInput {box-shadow: 2px 3px 1px rgba(0,0,0,0.2);}
        .block-container {padding-bottom: 0rem;}
        .css-18e3th9 {padding-top: 0rem; padding-bottom: 0rem;}
        .css-ocqkz7 {gap: 0rem 1rem;}
        .e1fqkh3o1 {box-shadow: 0 3px 3px rgba(0,0,0,0.2);}
        .e1wqxbhn2 {background: rgba(255,255,255,0.95);}
        .edgvbvh9 {border: 2px solid #b16ee6; margin: 2px; min-width: 155px; min-height: 60px;}
        .e1fqkh3o3 {background: rgba(255,255,255,0.95);}
        .e1fqkh3o5 {padding-top: 0.5em; padding-bottom: 0.5rem;}}
        .css-mp6ck8 {border: 2px solid #b16ee6; min-width: 155px; min-height: 60px;}
        .css-50ug3q {color: #593773}
        """
    append_tag = f'<style>{default}</style>'
    
    return append_tag

def crew_chiefs():
    return {
        "Lampkin" : {"subcontractor" : "C.T. Male", "no." : "518-775-6702", "email" : "r.lampkin@ctmale.com"},
        "Skelly" : {"subcontractor" : "C.T. Male", "no." : "518-262-9999", "email" : "r.skelly@ctmale.com"},
        "Ellison" : {"subcontractor" : "C.T. Male", "no." : "351-555-9876"}
    }
    
def get_state_vars():   
    state_vars = {
        'login_error' : False,
        'logged_in' : False,
        'login_error_message' : '',
        'page' : 'login',
        'login_form_username' : '',
        'login_form_username_key' : '',
        'login_form_pass': '',
        'login_form_pass_key' : '',
        'multiselect_structure_filter' : [],
        'pm_conflicts_only': False,
        'pm_sort_by' : 'Stage',
        'pm_sort_toggle' : False,
        }

    return state_vars

def initialize_state_variables():
    # Initialize state variables on page load
    for _ in get_state_vars():
        if _ not in st.session_state:
            st.session_state[_] = get_state_vars()[_] 

def project_stages(selection=0):
    details = {
        "planning" : {"display_name": "🗂️ Planning", "next" : "stakeout", "subcontractor" : "Burns McDonnell", "team" : "Project Mgmt", "duration_days" : 10, "dual_stage" : True, "stage_order" : 1},
        "stakeout" : {"display_name": "🧭 Stakeout", "next" : "clearing", "subcontractor" : "C.T. Male", "team" : "Survey", "duration_days" : 1, "dual_stage" : True, "stage_order" : 3},
        "brush clearing" : {"display_name": "🌿 Brush clearing", "next" : "stakeout", "subcontractor" : "Supreme", "team" : "Constr.", "duration_days" : 1, "dual_stage" : True, "stage_order" : 2},
        "clearing" : {"display_name": "🪵 Clearing", "next" : "construction", "subcontractor" : "Supreme", "team" : "Constr.", "duration_days" : 1, "dual_stage" : True, "stage_order" : 4},
        "construction" : {"display_name": "🚧 Construction", "next" : "survey offsets", "subcontractor" : "Supreme", "team" : "Constr.", "duration_days" : 4, "dual_stage" : False, "stage_order" : 5},
        "survey offsets" : {"display_name": "🔭 Survey offsets", "next" : "drilling", "subcontractor" : "C.T. Male", "team" : "Survey", "duration_days" : 1, "dual_stage" : False, "stage_order" : 6},
        "drilling" : {"display_name": "🏗️ Drilling", "next" : "line crew", "subcontractor" : "Tri State", "team" : "Drilling", "duration_days" : 4, "dual_stage" : False, "stage_order" : 7},
        "line crew" : {"display_name": "🔩 Line crew", "next" : "live wire", "subcontractor" : "3 Phase", "team" : "Electric", "duration_days" : 3, "dual_stage" : False, "stage_order" : 8},
        "live wire" : {"display_name": "⚡ Live wire", "next" : "as-built", "subcontractor" : "Burns McDonnell", "team" : "Project Mgmt", "duration_days" : 1, "dual_stage" : False, "stage_order" : 9},
        "monitoring" : {"display_name": "🎯 Monitoring", "next" : "live wire", "subcontractor" : "C.T. Male", "team" : "Survey", "duration_days" : 10, "dual_stage" : False, "stage_order" : 10},
        "as-built" : {"display_name": "📸 As-built", "next" : "monitoring", "subcontractor" : "C.T. Male", "team" : "Survey", "duration_days" : 1, "dual_stage" : True, "stage_order" : 11},
        }
    if selection == 0:
        return details
    else:
        return {_:details[_][selection] for _ in details}
   
def project_display_names():
    return {
        "🗂️ Planning" : "planning",
        "🧭 Stakeout" : "stakeout", 
        "🌿 Brush clearing" : "brush clearing", 
        "🪵 Clearing" : "clearing",
        "🚧 Construction" : "construction", 
        "🔭 Survey offsets" : "survey offsets", 
        "🏗️ Drilling" : "drilling",
        "🔩 Line crew" : "line crew",
        "⚡ Live wire" : " live wire",
        "🎯 Monitoring" : "monitoring", 
        "📸 As-built" : "as-built",
    }

def set_page_confige():
    st.set_page_config(
        layout='wide', initial_sidebar_state='collapsed', 
        page_title='C.T. Male', 
        menu_items=None
        )
