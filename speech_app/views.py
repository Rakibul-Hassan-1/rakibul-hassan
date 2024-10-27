# speech_app/views.py
from django.shortcuts import render
from .utils import speech_to_text, normalize_text
import difflib
import string
from .utils import speech_to_text, normalize_text

def index(request):
    context = {}
    if request.method == 'POST':
        transcript = request.POST['transcript']
        audio_file = request.FILES['audiofile']
        converted_text = speech_to_text(audio_file)

        # Normalize texts
        normalized_original = normalize_text(transcript)
        normalized_converted = normalize_text(converted_text)
        
        # Split normalized texts into words
        original_words = normalized_original.split()
        converted_words = normalized_converted.split()

        # Calculate the simple match accuracy
        s = difflib.SequenceMatcher(None, original_words, converted_words)
        matches = sum(n for i, j, n in s.get_matching_blocks())
        total_words = len(original_words)
        accuracy = (matches / total_words) * 100 if total_words > 0 else 0

        # Prepare display of comparison (use original non-normalized texts for display)
        original_display, converted_display = [], []
        for opcode in s.get_opcodes():
            tag, i1, i2, j1, j2 = opcode
            if tag == 'equal':
                original_display.append(' '.join(transcript.split()[i1:i2]))
                converted_display.append(' '.join(converted_text.split()[j1:j2]))
            elif tag == 'replace':
                original_display.append(f"<span style='background-color: yellow;'>{' '.join(transcript.split()[i1:i2])}</span>")
                converted_display.append(f"<span style='background-color: yellow;'>{' '.join(converted_text.split()[j1:j2])}</span>")
            elif tag == 'delete':
                original_display.append(f"<span style='background-color: red;'>{' '.join(transcript.split()[i1:i2])}</span>")
            elif tag == 'insert':
                converted_display.append(f"<span style='background-color: green;'>{' '.join(converted_text.split()[j1:j2])}</span>")

        context.update({
            'original_html': ' '.join(original_display),
            'converted_html': ' '.join(converted_display),
            'accuracy': f"{accuracy:.2f}%"  # Format accuracy to two decimal places
        })

    return render(request, 'speech_app/index.html', context)
