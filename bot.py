# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import requests
from collections import OrderedDict

app = Flask(__name__)

ORIGINAL_API = "https://infoff.vercel.app/info"

@app.route('/api/v2/userinfo', methods=['GET'])
def new_api():
    try:
        region = request.args.get('loc')
        user_id = request.args.get('id')
        
        if not all([region, user_id]):
            return jsonify({"error": "معلومات ناقصة"}), 400

        params = {'region': region, 'uid': user_id}
        response = requests.get(ORIGINAL_API, params=params)
        
        if response.status_code != 200:
            return jsonify({"error": "خطأ في السيرفر"}), 502

        original_data = response.json()
        processed_data = OrderedDict()
        
        # معلومات المطور
        processed_data["developer_info"] = {
            "telegram": "@zox_z8",
            "rights": "حقوق النشر محفوظة © 2024"
        }
        
        # استبعاد المفتاح "@checkinfo132"
        for key in original_data:
            if key != "@checkinfo132":
                processed_data[key] = original_data[key]
        
        return jsonify(processed_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500