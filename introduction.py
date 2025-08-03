import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
import base64

st.set_page_config(page_title="Pranay's Portfolio", layout="wide")
# Load and encode the image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Image in base64
encoded_image = get_base64_image("h.png")
profile_image = f"data:image/jpeg;base64,{encoded_image}"

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap');

/* Global style */
html, body, [class*="css"] {
    font-family: 'Roboto Slab', serif;
    background-color: #f6f6f9;
    color: black;
}

/* Title and subtitle */
.main-title {
    font-size: 48px;
    font-weight: 700;
    color: black;
    display: flex;
    align-items: center;
    gap: 10px;
}
.subtitle {
    font-size: 20px;
    color: #444;
}

/* Card styling */
.feature-card {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 4px 14px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
    color: black;
}
.tech-card {
    background: white;
    padding: 1.2rem;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin: 0.5rem;
    text-align: center;
    color: black;
}
.gif-icon {
    width: 32px;
    height: 32px;
    margin-right: 10px;
    vertical-align: middle;
}

/* ⚠️ Stronger override for expander body */
details > div[role="group"], .st-expanderContent {
    background-color: white !important;
    color: black !important;
    border-radius: 0 0 1rem 1rem;
    padding: 1.25rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)
name_desc,profile_photo = st.columns([8,1])
with name_desc:
    # --- Header ---
    wave_gif = "https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif"
    st.markdown(
        f"""
        <div class='main-title' style='color: #1DB954; font-size: 60px; font-weight: bold;'>
            Hey, I'm Pranay <img src='{wave_gif}' width='40'>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class='main-title' style='color: #1DB954; font-size: 25px; font-weight: bold;'>
        Data Scientist | Gen-AI Engineer | Lazy Coder | Problem Solver
        </div>

        <div class='sub-text' style='color: #1DB954; font-size: 20px; font-weight: bold;'>
        🧠 Turning Complexity into Clarity — One Line of Code at a Time.
        </div>

        <div class='sub-text' style='color: #1DB954; font-size: 20px; font-weight: bold;'>
        👋 Hey there! I’m Pranay Dilip Paipare
        </div>

        <div class='sub-text' style='color: #1DB954; font-size: 20px; font-weight: bold;'>
        A Data Scientist by title, a Generative AI Engineer by passion, and a lazy coder by design but the smart kind of lazy. I automate the boring, simplify the complex, and occasionally build tools that feel suspiciously like magic. ✨
        </div>

        <div class='sub-text' style='color: #1DB954; font-size: 20px; font-weight: bold;'>
        Over the last 2+ years, I’ve explored the wild terrains of sustainability, manufacturing, and supply chain — finding elegant AI solutions to gritty real-world problems. My sweet spot? Sitting right at the crossroads of business logic and AI wizardry.
        </div>
        """,
        unsafe_allow_html=True
    )

with profile_photo:
    st.image(profile_image, width=220)

st.write("")

# --- About ---
st.markdown(
    """
    <h3 style='color: #9333EA; margin-bottom: 0;'>🙋‍♂️ About Me</h3>
    <hr style='border: 2px solid #9333EA; margin-top: 0.2rem;'>
    """,
    unsafe_allow_html=True
)

designing = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
graph = "https://cdn-icons-png.flaticon.com/512/684/684908.png"
optimization = "https://cdn-icons-png.flaticon.com/512/2203/2203170.png"

ab1,ab2 = st.columns([1,1])
with ab1:
    st.markdown(f"""
    <div style="background-color: #f0f0f0; padding: 2rem; border-radius: 15px; color: black;
                font-family: 'Roboto Slab', serif; font-size: 16px; line-height: 1.6;">


    <h4 style="color: black; margin-bottom: 0.5rem; line-height: 1.0;"">🚀 What gets me out of bed (besides coffee)</h4>
    <ul>
        <li>🪄 Designing Gen-AI workflows so intuitive, even your boss wants to take them for a spin</li>
        <li>🕵️ Using graph databases to map out factory logic like a detective on a Netflix special</li>
        <li>🎯 Creating sourcing optimizers that make procurement feel like a strategy game</li>
        <li>⚙️ Making automation cool enough to make your Excel sheets feel jealous</li>
    </ul>

    <h4 style="color: black;">🏆 Highlights a.k.a. “I actually did stuff”</h4>
    <ul>
        <li>🧠 Built a Generative AI chatbot used by 30+ sustainability stakeholders to cut down repetitive work</li>
        <li>🏭 Designed a manufacturing recommender system that thinks faster than the floor manager</li>
        <li>📈 Created a vendor sourcing optimizer that reduced manual effort by 80%</li>
        <li>🚚 Engineered a logistics traceability tool accurate enough to make GPS nervous</li>
        <li>💡 Developed Gen-AI pipelines that turn business documents into structured gold</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)
with ab2:
    st.markdown(f"""
    <div style="background-color: #f0f0f0; padding: 2rem; border-radius: 15px; color: black;
                font-family: 'Roboto Slab', serif; font-size: 16px; line-height: 1.6;">

    <h4 style="color: black;">🎯 My Philosophy</h4>
    <li>♻️ Repetition? I automate. Chaos? I diagram. Complexity? I simplify.</li>
  <li>🛠️ If it saves time, clears clutter, or sparks clarity — I’m already building it.</li>
                
    <h4 style="color: black;">💡 Fun Fact</h4>
    <p>If I ever say “this is a one-line fix,” you should probably clear your schedule. <br>
    But if you’re stuck on something tricky? I’m your guy. Solving is fun. Coding is optional.</p>

    <h4 style="color: black;">🌌 Hobbies & Interests That Keep Me Grounded</h4>
    <ul>
        <li>🚀 Stargazing into space and the cosmos — because my curiosity has escape velocity</li>
        <li>✈️ Aerospace tech — where my love for logic literally takes flight</li>
        <li>🏎️ Automobiles — because I like my engines loud and my code louder</li>
    </ul>

                
    </div>
    """, unsafe_allow_html=True)

# --- Sections ---

colored_header("🚀 Projects & What I Build", description=None, color_name="violet-70")

col3, col4 = st.columns(2)

with col3:
    # ---------------- Sustainability Gen-AI -------------------
    with st.container():
        st.markdown("""
            <div style='background-color: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.1); color: black;'>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <h3 style="margin: 0; color: black;">Sustainability Gen-AI Tool</h3>
                </div>
                <p style="margin-top: 0.5rem;">♻️ Designed and deployed a full-stack Gen-AI chatbot, seamlessly integrated with a React-based interface, tailored for sustainability analytics. The chatbot intelligently parsed complex emissions datasets, identified high-impact carbon sources across the supply chain, and delivered contextualized insights to over 30 business stakeholders. By automating data interpretation and report generation, the solution reduced external vendor dependency and cut down query resolution time by 40%, while supporting high-volume data analysis at scale—all without compromising on accuracy or interpretability.</p>
        """, unsafe_allow_html=True)
        with st.expander("🔍 Show Details"):
            st.markdown("""
            <div style='background-color: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.1); color: black;'>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <h3 style="margin: 0; color: black;">Sustainability Gen-AI Tool</h3>
                </div>
                <p style="margin-top: 0.5rem;">
                Problem Statement:
                Solution Approach:
                Value obtained:</p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- Manufacturing Intelligence -------------------
    with st.container():
        st.markdown("""
            <div style='background-color: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.1); color: black;'>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <h3 style="margin: 0; color: black;">Manufacturing Intelligence</h3>
                </div>
                <p>🏭 Engineered a Gen-AI platform powered by graph databases to map intricate manufacturing workflows and production line logic with node-based precision. The system leveraged real-time sensor data and vector embeddings to detect anomalies 22% faster and identify root causes of equipment failures using semantic querying. Additionally, integrated a context-aware recommendation engine that proactively suggested resolution strategies—reducing average downtime by 25% and improving plant-wide operational efficiency by 12%, all while simplifying technical troubleshooting for frontline teams.</p>
        """, unsafe_allow_html=True)
        with st.expander("🔍 Show Details"):
            st.markdown("""
                <div style="color: black;">
                - Graph DBs (Neo4j) for component-process visualization<br>
                - LangChain-powered GenAI assistant for issue resolution<br>
                - Personalized recommendations for equipment ops<br><br>

                <strong>Impact:</strong><br>
                - Reduced downtime by 25%<br>
                - Improved anomaly detection by 22%
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- Network Intelligence -------------------
    with st.container():
        st.markdown("""
            <div style='background-color: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.1); color: black;'>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <h3 style="margin: 0; color: black;">Network Intelligence</h3>
                </div>
                <p>📊 Developed a graph-based Gen-AI solution with embedded LLM capabilities to answer complex Supply Chain Demand & Planning queries—leveraging knowledge graphs to trace dependencies across products, plants, and SKUs. The system visualizes the end-to-end journey of finished goods (FG), highlighting nodes and transitions across procurement, manufacturing, and logistics checkpoints. This multimodal interface enables users to interact with a dynamic graph, ask natural language questions, and receive explainable insights—enhancing visibility, improving planning accuracy by 27%, and accelerating RCA (root-cause analysis) during disruptions.</p>
        """, unsafe_allow_html=True)
        with st.expander("🔍 Show Details"):
            st.markdown("""
                <div style="color: black;">
                - Layered network view of machine-form-material mappings<br>
                - Helped factory floor managers identify bottlenecks fast<br>
                - Conversational UI over manufacturing data<br><br>

                <strong>Impact:</strong><br>
                - Cut tracing time by 28%<br>
                - Reduced back-and-forth between ops and IT
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


with col4:
    # ---------------- Batch-Level Tracing -------------------
    with st.container():
        st.markdown("""
            <div style='background-color: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.1); color: black;'>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <h3 style="margin: 0; color: black;">Batch-Level Tracing</h3>
                </div>
                <p>🚛 Designed an end-to-end logistics intelligence system at the batch level, enabling granular tracking across 40+ critical delivery checkpoints. The solution decoded hidden bottlenecks and uncovered previously untracked intermediate halts using geospatial clustering and temporal analysis. Integrated dynamic ETA prediction and route optimization logic to enhance finished goods traceability—boosting operational efficiency by 32% and reducing overall delivery delays across the supply chain by 38%, while minimizing manual intervention in logistics planning.</p>
        """, unsafe_allow_html=True)
        with st.expander("🔍 Show Details"):
            st.markdown("""
                <div style="color: black;">
                - Identified intermediate stops from plant to customer<br>
                - Dock-level granularity enabled via smart clustering<br>
                - Integrated with Power BI and Databricks<br><br>

                <strong>Impact:</strong><br>
                - Improved logistics precision by 38%<br>
                - Reduced delivery errors significantly
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- Sourcing Optimization -------------------
    with st.container():
        st.markdown("""
            <div style='background-color: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.1); color: black;'>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <h3 style="margin: 0; color: black;">Sourcing Optimization</h3>
                </div>
                <p>📦 Built a dynamic vendor selection platform combining linear programming and Particle Swarm Optimization (PSO) to balance competing priorities—cost, lead time, quality, and sustainability. Wrapped the engine in an intuitive Streamlit app that enabled procurement teams to perform scenario-based trade-off analysis through interactive dashboards. The hybrid optimization approach improved sourcing agility, reduced manual evaluation time by 80%, and enabled data-backed decisions aligned with long-term supplier strategy and environmental goals.</p>
        """, unsafe_allow_html=True)
        with st.expander("🔍 Show Details"):
            st.markdown("""
                <div style="color: black;">
                - Linear programming for vendor allocation<br>
                - Factored cost, emissions, quality, lead time, etc.<br>
                - Streamlit dashboard with sliders & thresholds<br><br>

                <strong>Impact:</strong><br>
                - 80% faster vendor selection<br>
                - Reduced over-reliance on a single supplier
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- LLM Training -------------------
    with st.container():
        st.markdown("""
            <div style='background-color: white; padding: 1.5rem; border-radius: 1rem; box-shadow: 0 4px 14px rgba(0,0,0,0.1); color: black;'>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <h3 style="margin: 0; color: black;">LLM Training</h3>
                </div>
                <p>  🧠 Fine-tuned a multimodal Large Language Model (LLM) using Low-Rank Adaptation (LoRA) to process and reason over both text and image inputs—enabling it to answer context-aware visual questions, generate image captions, and extract structured insights from unstructured multimedia data. Optimized training pipelines to reduce GPU memory usage by 65% while maintaining accuracy across tasks. The LoRA-powered adaptation approach made rapid experimentation scalable, accelerating downstream application development across knowledge extraction, product tagging, and multimodal search use cases.</p>
        """, unsafe_allow_html=True)
        with st.expander("🔍 Show Details"):
            st.markdown("""
                <div style="color: black;">
                - Linear programming for vendor allocation<br>
                - Factored cost, emissions, quality, lead time, etc.<br>
                - Streamlit dashboard with sliders & thresholds<br><br>

                <strong>Impact:</strong><br>
                - 80% faster vendor selection<br>
                - Reduced over-reliance on a single supplier
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)



# --- Skills & Tools ---
colored_header("🛠 Tech Stack & Skills", description=None, color_name="blue-70")

cols = st.columns(4)
tools = [
    ("Python", "https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif"),
    ("LangChain / LangGraph", "https://media.giphy.com/media/l0HlOvJ7yaacpuSas/giphy.gif"),
    ("Azure", "https://media.giphy.com/media/3orieZ4eKfG5hWsxEk/giphy.gif"),
    ("Databricks", "https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif"),
    ("Neo4j", "https://media.giphy.com/media/f9k1tV7HyORcngKF8v/giphy.gif"),
    ("SQL", "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"),
    ("Streamlit", "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif"),
    ("Vector DBs", "https://media.giphy.com/media/ZcK3n6XJ8gjHq/giphy.gif")
]

for i, (tool, gif) in enumerate(tools):
    with cols[i % 4]:
        st.markdown(f"<div class='tech-card'><img src='{gif}' class='gif-icon'><h4>{tool}</h4></div>", unsafe_allow_html=True)



# --- Footer ---
st.markdown("""
---
Built with ❤️ by Pranay | [📧 Email](mailto:paiparepranay@gmail.com) | [🔗 LinkedIn](https://www.linkedin.com/in/pranay-paipare/)
""")