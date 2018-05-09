from flask import Flask, jsonify, request, abort
from google.cloud import translate

app = Flask(__name__)

@app.route('/ZKTranslate/translate', methods=['POST'])
def doTranslate():
    content = request.json
    print(content)
    tc = translate.Client()
    translations = []
    
    for locale in content['target_language']:
        translations.append("<data name='{}' xml:space='preserve'><value>{}</value></data>"
                    .format(content['key'],
                    tc.translate(content['text'], target_language=locale)['translatedText']))
        data = {
            'original_text': content['text'],
            'translation': translations}
        messages = None

    return jsonify ({'errors': messages,'meta': None,'data':data})
