import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Community Volunteering App",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- SESSION STATE ----------
if "menu" not in st.session_state:
    st.session_state.menu = None

if "profile_option" not in st.session_state:
    st.session_state.profile_option = None

if "post_type" not in st.session_state:
    st.session_state.post_type = None

if "permission" not in st.session_state:
    st.session_state.permission = None

# New session state for dashboard
if "activities" not in st.session_state:
    st.session_state.activities = []

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# ---------- UTILITY FUNCTIONS ----------
def apply_dark_mode():
    """Apply dark mode styles if enabled."""
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        .stApp {
            background-color: #121212;
            color: #ffffff;
        }
        .stSidebar {
            background-color: #1e1e1e;
        }
        .stButton>button {
            background-color: #310ce9;
            color: white;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>select {
            background-color: #2e2e2e;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

# ---------- PAGE FUNCTIONS ----------
def main_screen():
    """Main landing page."""
    st.title("🤝 Community Volunteering App")
    st.write("Welcome to the Helpize Community Volunteering App. Click ☰ (top-left) to open the menu and explore features like Profile, Posts, Settings, and Help.")
    st.markdown("""
    ---
    **2026 Helpize Community App.**
    """)

def profile_page():
    """Profile page with options."""
    st.header("👤 Profile")
    st.write("Manage your personal volunteering activities and preferences.")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("My Posts", use_container_width=True):
            st.session_state.profile_option = "My Posts"
            st.session_state.post_type = None
            st.session_state.permission = None
            st.rerun()
    with col2:
        if st.button("Registered Events", use_container_width=True):
            st.session_state.profile_option = "Registered Events"
            st.session_state.post_type = None
            st.session_state.permission = None
            st.rerun()
    with col3:
        if st.button("Liked Posts", use_container_width=True):
            st.session_state.profile_option = "Liked Posts"
            st.session_state.post_type = None
            st.session_state.permission = None
            st.rerun()

def my_posts_page():
    """My Posts sub-page."""
    st.subheader("📌 My Posts")
    st.write("View and manage your posted events.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Public", use_container_width=True):
            st.session_state.post_type = "Public"
            st.session_state.permission = None
            st.rerun()
    with col2:
        if st.button("Private", use_container_width=True):
            st.session_state.post_type = "Private"
            st.session_state.permission = None
            st.rerun()

def public_page():
    """Public event page."""
    st.subheader("🌍 Public Event")
    st.write("Review this public event post for community guidelines compliance.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Accepted", use_container_width=True):
            st.session_state.permission = "Accepted"
            st.session_state.menu = "Dashboard"
            st.rerun()
    with col2:
        if st.button("Denied", use_container_width=True):
            st.session_state.permission = "Denied"
            st.rerun()

def private_page():
    """Private event page."""
    st.subheader("🔒 Private Event")
    st.write("Review this private event post for community guidelines compliance.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Accepted", use_container_width=True):
            st.session_state.permission = "Accepted"
            st.session_state.menu = "Dashboard"
            st.rerun()
    with col2:
        if st.button("Denied", use_container_width=True):
            st.session_state.permission = "Denied"
            st.rerun()

def registered_events_page():
    st.subheader("📝 Registered Events")
    st.write("Here is a list of events you have joined. (Placeholder for actual data)")

def liked_posts_page():
    st.subheader("❤️ Liked Posts")
    st.write("Posts you have favorited. (Placeholder for actual data)")

def posts_page():
    st.header("📢 Posts Page")
    st.write("Global feed of all volunteer opportunities. (Placeholder for actual feed)")

def settings_page():
    st.header("⚙️ Settings")
    st.write("Manage your account and notifications. (Placeholder for settings)")

def help_page():
    st.header("❓ Help")
    st.write("Frequently Asked Questions and Support. (Placeholder for FAQ)")

# ---------- DASHBOARD FUNCTIONS ----------
def dashboard_page():
    """Volunteer Dashboard page."""
    st.header("📊 Volunteer Dashboard")
    st.write("Manage your activities and events here.")
    
    # Dark mode toggle
    if st.button("Toggle Dark Mode 🌙/☀️"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()
    
    apply_dark_mode()
    
    # Tabs for navigation
    tab1, tab2 = st.tabs(["Submit Activity", "View Activities"])
    
    with tab1:
        submit_activity()
    
    with tab2:
        view_activities()

def submit_activity():
    """Submit Activity form."""
    st.subheader("Submit Activity")
    with st.form("activity_form", clear_on_submit=True):
        st.markdown("### Activity Details")
        registration_link = st.text_input("Registration Link", placeholder="https://example.com", help="Provide a link for registration.")
        activity_file = st.file_uploader("Upload Activity File (Optional)", type=["pdf", "doc", "docx"], help="Upload supporting documents.")
        date = st.date_input("Date", min_value=datetime.today(), help="Select the event date.")
        place = st.text_input("Place", placeholder="e.g., City Hall", help="Location of the event.")
        about_event = st.text_area("About the Event", placeholder="Describe the event...", height=100, help="Detailed description.")
        cause = st.selectbox("Cause", ["Select Cause", "Disaster Relief", "Community Help", "Environmental", "Health", "Education", "Other"], help="Choose the cause category.")
        poster = st.file_uploader("Poster (Image Upload)", type=["jpg", "png", "jpeg"], help="Upload an event poster.")
        
        submitted = st.form_submit_button("Submit Activity", use_container_width=True)
        if submitted:
            if not (registration_link and date and place and about_event and cause != "Select Cause" and poster):
                st.error("Please fill all required fields marked with *.")
            else:
                activity = {
                    "registration_link": registration_link,
                    "activity_file": activity_file.name if activity_file else None,
                    "date": str(date),
                    "place": place,
                    "about_event": about_event,
                    "cause": cause,
                    "poster": poster.name if poster else "No file"
                }
                st.session_state.activities.append(activity)
                st.success("Activity submitted successfully!")
                st.rerun()

def view_activities():
    """View Activities list."""
    st.subheader("Recent Activities")
    if not st.session_state.activities:
        st.info("No activities yet. Submit one on the Submit Activity tab to get started!")
    else:
        for i, activity in enumerate(st.session_state.activities):
            with st.expander(f"Activity {i+1}: {activity['about_event']}"):
                st.write(f"**Date:** {activity['date']}")
                st.write(f"**Place:** {activity['place']}")
                st.write(f"**Cause:** {activity['cause']}")
                st.write(f"**Registration Link:** [{activity['registration_link']}]({activity['registration_link']})")
                st.write(f"**Poster:** {activity['poster']}")
                if activity['activity_file']:
                    st.write(f"**File:** {activity['activity_file']}")

# ---------- SIDEBAR (☰ MENU) ----------
with st.sidebar:
    st.title("Menu")
    if st.button("🏠 Home"):
        st.session_state.menu = None
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("👤 Profile"):
        st.session_state.menu = "Profile"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("📢 Posts"):
        st.session_state.menu = "Posts"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("⚙️ Settings"):
        st.session_state.menu = "Settings"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("❓ Help"):
        st.session_state.menu = "Help"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()

# ---------- MAIN LOGIC ----------
apply_dark_mode()  # Apply dark mode globally

if st.session_state.menu is None:
    main_screen()
elif st.session_state.menu == "Profile":
    if st.session_state.profile_option is None:
        profile_page()
    elif st.session_state.profile_option == "My Posts":
        if st.session_state.post_type is None:
            my_posts_page()
        elif st.session_state.post_type == "Public":
            public_page()
        elif st.session_state.post_type == "Private":
            private_page()
    elif st.session_state.profile_option == "Registered Events":
        registered_events_page()
    elif st.session_state.profile_option == "Liked Posts":
        liked_posts_page()
elif st.session_state.menu == "Posts":
    posts_page()
elif st.session_state.menu == "Dashboard":
    if st.session_state.permission == "Accepted":
        dashboard_page()
    else:
        st.error("Access denied. Please follow the proper flow to access the Dashboard.")
        st.session_state.menu = None
        st.rerun()
elif st.session_state.menu == "Settings":
    settings_page()
elif st.session_state.menu == "Help":
    help_page()

# ---------- RESULT (Conditional Display) ----------
if st.session_state.permission == "Denied":
    st.error("❌ Permission Denied - Please review and resubmit.")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("**© 2026 Helpize Community App. All rights reserved.**")