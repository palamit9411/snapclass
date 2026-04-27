from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io
import librosa
import streamlit as st



@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        st.error('Voice recog error')
        return None
    


def identify_speaker(new_embedding, candidates_dict, threshold=0.5):

    if new_embedding is None or not candidates_dict:
        return None, 0.0
    
    best_sid = None
    best_score = -1

    for sid, stored_embedding in candidates_dict.items():
        if stored_embedding:

            new_emb = np.array(new_embedding)
            stored_emb = np.array(stored_embedding)

            similarity = np.dot(new_emb, stored_emb) / (
                np.linalg.norm(new_emb) * np.linalg.norm(stored_emb)
            )

            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_score, best_sid
    
    return None, best_score



def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):

    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        segments = librosa.effects.split(audio, top_db=20)
        # st.write("Segments:", segments)

        identified_results = {}

        for start, end in segments:

            if (end-start) < sr * 0.5:
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)


            score, sid = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error(f'Bulk process error')
        return {}