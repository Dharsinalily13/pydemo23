import streamlit as st

st.set_page_config(page_title="Community Volunteering App")

# ---------- SESSION STATE ----------
if "menu" not in st.session_state:
    st.session_state.menu = None

if "profile_option" not in st.session_state:
    st.session_state.profile_option = None

if "post_type" not in st.session_state:
    st.session_state.post_type = None

if "permission" not in st.session_state:
    st.session_state.permission = None

# ---------- PAGE FUNCTIONS ----------
def main_screen():
    """Main landing page."""
    st.title("🤝 Community Volunteering App")
    st.write("Click ☰ (top-left) to open menu")

def profile_page():
    """Profile page with options."""
    st.header("👤 Profile")
    if st.button("My Posts"):
        st.session_state.profile_option = "My Posts"
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("Registered Events"):
        st.session_state.profile_option = "Registered Events"
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("Liked Posts"):
        st.session_state.profile_option = "Liked Posts"
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()

def my_posts_page():
    """My Posts sub-page."""
    st.subheader("📌 My Posts")
    if st.button("Public"):
        st.session_state.post_type = "Public"
        st.session_state.permission = None
        st.rerun()
    if st.button("Private"):
        st.session_state.post_type = "Private"
        st.session_state.permission = None # Reset permission when switching
        st.rerun()

def public_page():
    """Public event page."""
    st.subheader("🌍 Public Event")
    st.write("Does this post meet community guidelines?")
    if st.button("Accepted"):
        st.session_state.permission = "Accepted"
        st.rerun()
    if st.button("Denied"):
        st.session_state.permission = "Denied"
        st.rerun()

def private_page():
    """Private event page - MODIFIED: Removed permission buttons."""
    st.subheader("🔒 Private Event")
    st.info("This is a private event. Content is restricted to members only.")
    st.session_state.permission = None  # Ensure no Accepted/Denied message shows here
    
    if st.button("Back to My Posts"):
        st.session_state.post_type = None
        st.rerun()

def registered_events_page():
    st.subheader("📝 Registered Events")
    st.write("List of events you have joined.")

def liked_posts_page():
    st.subheader("❤️ Liked Posts")
    st.write("Posts you have favorited.")

def posts_page():
    st.header("📢 Posts Page")
    st.write("Global feed of all volunteer opportunities.")

def settings_page():
    st.header("⚙️ Settings")
    st.write("Manage your account and notifications.")

def help_page():
    st.header("❓ Help")
    st.write("Frequently Asked Questions and Support.")

# ---------- SIDEBAR (☰ MENU) ----------
with st.sidebar:
    if st.button("Profile"):
        st.session_state.menu = "Profile"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("Posts"):
        st.session_state.menu = "Posts"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("Settings"):
        st.session_state.menu = "Settings"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()
    if st.button("Help"):
        st.session_state.menu = "Help"
        st.session_state.profile_option = None
        st.session_state.post_type = None
        st.session_state.permission = None
        st.rerun()

# ---------- MAIN LOGIC ----------
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
elif st.session_state.menu == "Settings":
    settings_page()
elif st.session_state.menu == "Help":
    help_page()

# ---------- RESULT (Conditional Display) ----------
if st.session_state.permission == "Accepted":
    st.success("✅ Permission Accepted")
elif st.session_state.permission == "Denied":
    st.error("❌ Permission Denied")