# ==============================================================================
# Copyright (C) 2021 Evil0ctal
#
# This file is part of the Douyin_TikTok_Download_API project.
#
# This project is licensed under the Apache License 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

class Config:
    """配置管理类，用于从环境变量中读取配置"""
    
    def __init__(self):
        # 加载.env文件
        env_path = Path(__file__).parent.parent.parent / '.env'
        load_dotenv(env_path)
        
        # 抖音配置
        self.douyin = {
            'headers': {
                'Accept-Language': os.getenv('DOUYIN_ACCEPT_LANGUAGE', 'zh-CN,zh;q=0.9'),
                'User-Agent': os.getenv('DOUYIN_USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'),
                'Referer': os.getenv('DOUYIN_REFERER', 'https://www.douyin.com/'),
                'Cookie': os.getenv('DOUYIN_COOKIE', '')
            },
            'proxies': {
                'http': os.getenv('DOUYIN_HTTP_PROXY', None),
                'https': os.getenv('DOUYIN_HTTPS_PROXY', None)
            }
        }
        
        # TikTok配置
        self.tiktok = {
            'headers': {
                'Accept-Language': os.getenv('TIKTOK_ACCEPT_LANGUAGE', 'en-US,en;q=0.9'),
                'User-Agent': os.getenv('TIKTOK_USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'),
                'Referer': os.getenv('TIKTOK_REFERER', 'https://www.tiktok.com/'),
                'Cookie': os.getenv('TIKTOK_COOKIE', '')
            },
            'proxies': {
                'http': os.getenv('TIKTOK_HTTP_PROXY', None),
                'https': os.getenv('TIKTOK_HTTPS_PROXY', None)
            }
        }
        
        # API配置
        self.api = {
            'host': os.getenv('API_HOST', '0.0.0.0'),
            'port': int(os.getenv('API_PORT', '8000')),
            'debug': os.getenv('API_DEBUG', 'False').lower() == 'true',
            'workers': int(os.getenv('API_WORKERS', '1')),
            'timeout': int(os.getenv('API_TIMEOUT', '60'))
        }
    
    @property
    def douyin_headers(self) -> dict:
        """获取抖音请求头"""
        return self.douyin['headers']
    
    @property
    def douyin_proxies(self) -> Optional[dict]:
        """获取抖音代理配置"""
        return self.douyin['proxies']
    
    @property
    def tiktok_headers(self) -> dict:
        """获取TikTok请求头"""
        return self.tiktok['headers']
    
    @property
    def tiktok_proxies(self) -> Optional[dict]:
        """获取TikTok代理配置"""
        return self.tiktok['proxies']
    
    @property
    def api_settings(self) -> dict:
        """获取API服务配置"""
        return self.api

# 创建全局配置实例
env_config = Config()