import acoustid

def generate_audio_fingerprint(file_path):
    try:
        duration, fingerprint = acoustid.fingerprint_file(file_path)
        return fingerprint
    except acoustid.NoBackendError:
        print("Error: The Chromaprint library (libchromaprint) was not found.")
    except acoustid.FingerprintGenerationError:
        print("Error: Fingerprint generation failed.")
