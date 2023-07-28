import pyaudio

import wave

def grabar_audio(nombre_archivo, duracion_segundos, frecuencia_muestreo=44100, tamano_muestra=1024, canales=2):
    # Inicializar PyAudio
    p = pyaudio.PyAudio()

    # Configurar el stream de audio
    stream = p.open(format=pyaudio.paInt16,
                    channels=canales,
                    rate=frecuencia_muestreo,
                    input=True,
                    frames_per_buffer=tamano_muestra)

    # Lista para almacenar los fragmentos de audio grabados
    frames = []

    # Grabar audio en fragmentos
    for i in range(0, int(frecuencia_muestreo / tamano_muestra * duracion_segundos)):
        data = stream.read(tamano_muestra)
        frames.append(data)

    # Detener y cerrar el stream de audio
    stream.stop_stream()
    stream.close()

    # Terminar PyAudio
    p.terminate()

    # Crear el archivo WAV y guardar los fragmentos de audio
    with wave.open(nombre_archivo, 'wb') as wf:
        wf.setnchannels(canales)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(frecuencia_muestreo)
        wf.writeframes(b''.join(frames))

    print(f"¡Grabación completa! El archivo '{nombre_archivo}' ha sido guardado en formato WAV.")

# Ejemplo de uso: grabar 5 segundos de audio y guardarlo en un archivo llamado "mi_grabacion.wav"
grabar_audio("mi_grabacion.wav", duracion_segundos=5)
