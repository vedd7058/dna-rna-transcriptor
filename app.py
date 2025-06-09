
import streamlit as st
import re



st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmtwZzNnb3piazF5MGJudzBjN2d0OTBpb2FvbWE3d3RzZjFpZHJ2NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YrTJKOe0FhQJAUXTyp/giphy.gif");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.85;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(page_title="DNA to RNA Transcription Tool", layout="wide")



st.title("🧬 DNA → RNA Transcription Tool")

st.markdown("Enter your DNA sequence below:")

sequence = st.text_area("DNA Sequence", height=200)

def is_valid_dna(seq):
    return bool(re.fullmatch(r"[ATCGatcg\n ]+", seq))

def transcribe_dna_to_rna(dna_seq):
    return dna_seq.upper().replace("T", "U")

def reverse_complement(dna_seq):
    complement = {'A':'T','T':'A','G':'C','C':'G'}
    return "".join(complement.get(base.upper(), base) for base in reversed(dna_seq))

def gc_content(seq):
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return round((gc_count / len(seq)) * 100, 2) if len(seq) > 0 else 0

if sequence:
    sequence = sequence.replace("\n", "").replace(" ", "")
    if is_valid_dna(sequence):
        st.success("Valid DNA sequence ✅")

        rna = transcribe_dna_to_rna(sequence)
        rev_comp = reverse_complement(sequence)
        gc = gc_content(sequence)

        st.subheader("🔬 Results:")
        st.write("RNA Sequence:", rna)
        st.write("Reverse Complement:", rev_comp)
        st.write(f"GC Content: {gc}%")

        st.download_button("📥 Download RNA as TXT", data=rna, file_name="rna_sequence.txt")

    else:
        st.error("Invalid DNA sequence. Only A, T, G, C characters are allowed.")
