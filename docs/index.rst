.. enzyme documentation master file, created by
   sphinx-quickstart on Mon Feb 27 14:24:43 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============
Release v\ |version|

Python module to parse metadata in video files

Example
=======
You can parse any video file. If a parse error occurs, it will throw a ParseError exception.
To see what data has been parsed, you can print the object:

    >>> import enzyme
    >>> p = enzyme.parse('/mnt/movies/My Rips/Harry Potter and the Prisoner of Azkaban (2004)/Harry Potter And The Prisoner Of Azkaban (2004) - 1080p BluRay DTS x264.mkv')
    >>> print p
    |      title: Harry Potter And The Prisoner Of Azkaban (2004) - 1080p BluRay DTS x264
    |       type: Matroska
    |  timestamp: 1320680617
    |       mime: video/x-matroska
    |     length: 8502.176
    +-- Video Track #1
    |    |      title: Harry Potter And The Prisoner Of Azkaban (2004) - 1080p BluRay DTS x264
    |    |   language: eng
    |    |      codec: AVC1
    |    |      width: 1920
    |    |     height: 1080
    |    |        fps: 23.9760247425
    |    |     aspect: 1.77777777778
    |    |    trackno: 1
    |    |         id: 0
    |    | codec_private: <unprintable data, size=41>
    +-- Audio Track #1
    |    |      title: DTS French
    |    |   language: fre
    |    |   channels: 6
    |    | samplerate: 48000.0
    |    |      codec: 8193
    |    |    trackno: 2
    |    |         id: 0
    +-- Audio Track #2
    |    |      title: DTS English
    |    |   language: eng
    |    |   channels: 6
    |    | samplerate: 48000.0
    |    |      codec: 8193
    |    |    trackno: 3
    |    |         id: 1
    |    |    default: False
    +-- Audio Track #3
    |    |      title: AC3 Spanish
    |    |   language: spa
    |    |   channels: 6
    |    | samplerate: 48000.0
    |    |      codec: 8192
    |    |    trackno: 4
    |    |         id: 2
    |    |    default: False
    +-- Audio Track #4
    |    |      title: AC3 Italian
    |    |   language: ita
    |    |   channels: 6
    |    | samplerate: 48000.0
    |    |      codec: 8192
    |    |    trackno: 5
    |    |         id: 3
    |    |    default: False
    +-- Audio Track #5
    |    |      title: AC3 Dutch
    |    |   language: dut
    |    |   channels: 6
    |    | samplerate: 48000.0
    |    |      codec: 8192
    |    |    trackno: 6
    |    |         id: 4
    |    |    default: False
    +-- Subtitle #1
    |    |    default: False
    |    |   language: eng
    |    |    trackno: 7
    |    |      title: Complete(srt)
    |    |         id: 0
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #2
    |    |    default: False
    |    |   language: fre
    |    |    trackno: 8
    |    |      title: Complete(srt)
    |    |         id: 1
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #3
    |    |   language: fre
    |    |    trackno: 9
    |    |      title: Forced French
    |    |         id: 2
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #4
    |    |    default: False
    |    |   language: spa
    |    |    trackno: 10
    |    |      title: Complete(srt)
    |    |         id: 3
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #5
    |    |    default: False
    |    |   language: spa
    |    |    trackno: 11
    |    |      title: Forced Spanish
    |    |         id: 4
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #6
    |    |    default: False
    |    |   language: ita
    |    |    trackno: 12
    |    |      title: Complete(srt)
    |    |         id: 5
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #7
    |    |    default: False
    |    |   language: ita
    |    |    trackno: 13
    |    |      title: Forced Italian
    |    |         id: 6
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #8
    |    |    default: False
    |    |   language: dut
    |    |    trackno: 14
    |    |      title: Complete(srt)
    |    |         id: 7
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #9
    |    |    default: False
    |    |   language: dut
    |    |    trackno: 15
    |    |      title: Forced Dutch
    |    |         id: 8
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #10
    |    |    default: False
    |    |   language: fin
    |    |    trackno: 16
    |    |      title: Complete(srt)
    |    |         id: 9
    |    |      codec: S_TEXT/UTF8
    +-- Subtitle #11
    |    |    default: False
    |    |   language: nor
    |    |    trackno: 17
    |    |      title: Complete(srt)
    |    |         id: 10
    |    |      codec: S_TEXT/UTF8
    +-- Chapter #1
    |    |    enabled: 1
    |    |       name: 00:00:00.000
    |    |        pos: 0.0
    |    |         id: 0
    +-- Chapter #2
    |    |    enabled: 1
    |    |       name: 00:01:40.100
    |    |        pos: 100.1
    |    |         id: 1
    +-- Chapter #3
    |    |    enabled: 1
    |    |       name: 00:06:36.229
    |    |        pos: 396.229
    |    |         id: 2
    +-- Chapter #4
    |    |    enabled: 1
    |    |       name: 00:12:45.932
    |    |        pos: 765.932
    |    |         id: 3
    +-- Chapter #5
    |    |    enabled: 1
    |    |       name: 00:14:52.517
    |    |        pos: 892.517
    |    |         id: 4
    +-- Chapter #6
    |    |    enabled: 1
    |    |       name: 00:16:12.513
    |    |        pos: 972.513
    |    |         id: 5
    +-- Chapter #7
    |    |    enabled: 1
    |    |       name: 00:18:56.218
    |    |        pos: 1136.218
    |    |         id: 6
    +-- Chapter #8
    |    |    enabled: 1
    |    |       name: 00:23:50.387
    |    |        pos: 1430.387
    |    |         id: 7
    +-- Chapter #9
    |    |    enabled: 1
    |    |       name: 00:28:50.729
    |    |        pos: 1730.729
    |    |         id: 8
    +-- Chapter #10
    |    |    enabled: 1
    |    |       name: 00:31:21.838
    |    |        pos: 1881.838
    |    |         id: 9
    +-- Chapter #11
    |    |    enabled: 1
    |    |       name: 00:38:50.161
    |    |        pos: 2330.161
    |    |         id: 10
    +-- Chapter #12
    |    |    enabled: 1
    |    |       name: 00:44:45.308
    |    |        pos: 2685.308
    |    |         id: 11
    +-- Chapter #13
    |    |    enabled: 1
    |    |       name: 00:47:37.813
    |    |        pos: 2857.813
    |    |         id: 12
    +-- Chapter #14
    |    |    enabled: 1
    |    |       name: 00:49:39.935
    |    |        pos: 2979.935
    |    |         id: 13
    +-- Chapter #15
    |    |    enabled: 1
    |    |       name: 00:53:42.845
    |    |        pos: 3222.845
    |    |         id: 14
    +-- Chapter #16
    |    |    enabled: 1
    |    |       name: 00:57:28.403
    |    |        pos: 3448.403
    |    |         id: 15
    +-- Chapter #17
    |    |    enabled: 1
    |    |       name: 01:01:23.722
    |    |        pos: 3683.722
    |    |         id: 16
    +-- Chapter #18
    |    |    enabled: 1
    |    |       name: 01:03:22.924
    |    |        pos: 3802.924
    |    |         id: 17
    +-- Chapter #19
    |    |    enabled: 1
    |    |       name: 01:07:10.985
    |    |        pos: 4030.985
    |    |         id: 18
    +-- Chapter #20
    |    |    enabled: 1
    |    |       name: 01:11:53.476
    |    |        pos: 4313.476
    |    |         id: 19
    +-- Chapter #21
    |    |    enabled: 1
    |    |       name: 01:19:10.079
    |    |        pos: 4750.079
    |    |         id: 20
    +-- Chapter #22
    |    |    enabled: 1
    |    |       name: 01:22:29.945
    |    |        pos: 4949.945
    |    |         id: 21
    +-- Chapter #23
    |    |    enabled: 1
    |    |       name: 01:27:30.871
    |    |        pos: 5250.871
    |    |         id: 22
    +-- Chapter #24
    |    |    enabled: 1
    |    |       name: 01:30:13.366
    |    |        pos: 5413.366
    |    |         id: 23
    +-- Chapter #25
    |    |    enabled: 1
    |    |       name: 01:34:19.028
    |    |        pos: 5659.028
    |    |         id: 24
    +-- Chapter #26
    |    |    enabled: 1
    |    |       name: 01:36:56.894
    |    |        pos: 5816.894
    |    |         id: 25
    +-- Chapter #27
    |    |    enabled: 1
    |    |       name: 01:42:24.472
    |    |        pos: 6144.472
    |    |         id: 26
    +-- Chapter #28
    |    |    enabled: 1
    |    |       name: 01:45:40.334
    |    |        pos: 6340.334
    |    |         id: 27
    +-- Chapter #29
    |    |    enabled: 1
    |    |       name: 01:50:03.597
    |    |        pos: 6603.597
    |    |         id: 28
    +-- Chapter #30
    |    |    enabled: 1
    |    |       name: 01:55:33.343
    |    |        pos: 6933.343
    |    |         id: 29
    +-- Chapter #31
    |    |    enabled: 1
    |    |       name: 02:00:07.409
    |    |        pos: 7207.409
    |    |         id: 30
    +-- Chapter #32
    |    |    enabled: 1
    |    |       name: 02:03:16.055
    |    |        pos: 7396.055
    |    |         id: 31
    +-- Chapter #33
    |    |    enabled: 1
    |    |       name: 02:06:02.513
    |    |        pos: 7562.513
    |    |         id: 32
    +-- Chapter #34
    |    |    enabled: 1
    |    |       name: 02:08:42.924
    |    |        pos: 7722.924
    |    |         id: 33
    +-- Chapter #35
    |    |    enabled: 1
    |    |       name: 02:09:47.405
    |    |        pos: 7787.405
    |    |         id: 34

API Documentation
=================

Parser
------
.. automodule:: enzyme
    :members:

Core classes
------------
.. automodule:: enzyme.core
    :members:
