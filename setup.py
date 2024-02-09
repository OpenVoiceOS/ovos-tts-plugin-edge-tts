from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-tts-plugin-edge-tts = ovos_tts_plugin_edge_tts:EdgeTTSPlugin'

setup(
    name='ovos-tts-plugin-edge-tts',
    version='0.1',
    description='A tts plugin for OpenVoiceOS, using EdgeTTS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/timonvanhasselt/ovos-tts-plugin-edge-tts',
    author='Your Name',
    author_email='your@email.com',
    license='Apache-2.0',
    packages=['ovos_tts_plugin_edge_tts'],
    install_requires=[
        'edge-tts>=6.1.9',
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='ovos plugin tts edge-tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
