#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# parseit - Video metadata parser
# Copyright (C) 2011 Antoine Bertin <diaoulael@gmail.com>
#
# This file is part of parseit.
#
# parseit is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Subliminal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import os
import unittest
import logging
import os
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'parseit')))
import parseit


# Set up logging
logging.getLogger('parseit').setLevel(logging.DEBUG)

# matroska_test_w1_1 path
matroska_test_path = os.path.abspath(os.path.join('files', 'matroska_test_w1_1'))


class MKVTestCase(unittest.TestCase):
    tests = ['test_title', 'test_comment', 'test_type_mime_media', 'test_timestamp', 
             'test_datetime', 'test_length', 'test_tags', 'test_video', 'test_audio', 'test_subtitles']

    def setUp(self):
        self.p1 = parseit.parse(os.path.join(matroska_test_path, u'test1.mkv'))
        self.p2 = parseit.parse(os.path.join(matroska_test_path, u'test2.mkv'))
        self.p3 = parseit.parse(os.path.join(matroska_test_path, u'test3.mkv'))
        self.p4 = parseit.parse(os.path.join(matroska_test_path, u'test4.mkv'))
        self.p5 = parseit.parse(os.path.join(matroska_test_path, u'test5.mkv'))
        self.p6 = parseit.parse(os.path.join(matroska_test_path, u'test6.mkv'))
        self.p7 = parseit.parse(os.path.join(matroska_test_path, u'test7.mkv'))
        self.p8 = parseit.parse(os.path.join(matroska_test_path, u'test8.mkv'))

    def test_title(self):
        self.assertTrue(self.p1.title == 'Big Buck Bunny - test 1')
        self.assertTrue(self.p2.title == 'Elephant Dream - test 2')
        self.assertTrue(self.p3.title == 'Elephant Dream - test 3')
        #self.assertTrue(self.p4.title is None)
        self.assertTrue(self.p5.title == 'Big Buck Bunny - test 8')
        self.assertTrue(self.p6.title == 'Big Buck Bunny - test 6')
        self.assertTrue(self.p7.title == 'Big Buck Bunny - test 7')
        self.assertTrue(self.p8.title == 'Big Buck Bunny - test 8')

    def test_comment(self):
        self.assertTrue(self.p1.comment == 'Matroska Validation File1, basic MPEG4.2 and MP3 with only SimpleBlock')
        self.assertTrue(self.p2.comment == 'Matroska Validation File 2, 100,000 timecode scale, odd aspect ratio, and CRC-32. Codecs are AVC and AAC')
        self.assertTrue(self.p3.comment == 'Matroska Validation File 3, header stripping on the video track and no SimpleBlock')
        #self.assertTrue(self.p4.comment is None)
        self.assertTrue(self.p5.comment == 'Matroska Validation File 8, secondary audio commentary track, misc subtitle tracks')
        self.assertTrue(self.p6.comment == 'Matroska Validation File 6, random length to code the size of Clusters and Blocks, no Cues for seeking')
        self.assertTrue(self.p7.comment == 'Matroska Validation File 7, junk elements are present at the beggining or end of clusters, the parser should skip it. There is also a damaged element at 451418')
        self.assertTrue(self.p8.comment == 'Matroska Validation File 8, audio missing between timecodes 6.019s and 6.360s')

    def test_type_mime_media(self):
        self.assertTrue(self.p1.type == 'Matroska')
        self.assertTrue(self.p2.type == 'Matroska')
        self.assertTrue(self.p3.type == 'Matroska')
        #self.assertTrue(self.p4.type is None)
        self.assertTrue(self.p5.type == 'Matroska')
        self.assertTrue(self.p6.type == 'Matroska')
        self.assertTrue(self.p7.type == 'Matroska')
        self.assertTrue(self.p8.type == 'Matroska')
        self.assertTrue(self.p1.mime == 'video/x-matroska')
        self.assertTrue(self.p2.mime == 'video/x-matroska')
        self.assertTrue(self.p3.mime == 'video/x-matroska')
        #self.assertTrue(self.p4.mime is None)
        self.assertTrue(self.p5.mime == 'video/x-matroska')
        self.assertTrue(self.p6.mime == 'video/x-matroska')
        self.assertTrue(self.p7.mime == 'video/x-matroska')
        self.assertTrue(self.p8.mime == 'video/x-matroska')
        self.assertTrue(self.p1.media == 'MEDIA_AV')
        self.assertTrue(self.p2.media == 'MEDIA_AV')
        self.assertTrue(self.p3.media == 'MEDIA_AV')
        #self.assertTrue(self.p4.media is None)
        self.assertTrue(self.p5.media == 'MEDIA_AV')
        self.assertTrue(self.p6.media == 'MEDIA_AV')
        self.assertTrue(self.p7.media == 'MEDIA_AV')
        self.assertTrue(self.p8.media == 'MEDIA_AV')

    def test_timestamp(self):
        self.assertTrue(self.p1.timestamp == 1282375383)
        self.assertTrue(self.p2.timestamp == 1307018720)
        self.assertTrue(self.p3.timestamp == 1282427005)
        #self.assertTrue(self.p4.timestamp is None)
        self.assertTrue(self.p5.timestamp == 1282414003)
        self.assertTrue(self.p6.timestamp == 1282408315)
        self.assertTrue(self.p7.timestamp == 1282410023)
        self.assertTrue(self.p8.timestamp == 1282411334)

    def test_datetime(self):
        #TODO: Working?
        self.assertTrue(self.p1.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p2.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p3.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        #self.assertTrue(self.p4.datetime is None)
        self.assertTrue(self.p5.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p6.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p7.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p8.datetime == datetime.datetime(2010, 1, 1, 0, 0))

    def test_length(self):
        self.assertTrue(self.p1.length == 87.336)
        self.assertTrue(self.p2.length == 47.509)
        self.assertTrue(self.p3.length == 49.064)
        #self.assertTrue(self.p4.length is None)
        self.assertTrue(self.p5.length == 46.665)
        self.assertTrue(self.p6.length == 87.336)
        self.assertTrue(self.p7.length == 37.043)
        self.assertTrue(self.p8.length == 47.341)

    def test_tags(self):
        #TODO: Other properties
        self.assertTrue(self.p1.tags['comment'].value == 'Matroska Validation File1, basic MPEG4.2 and MP3 with only SimpleBlock')
        self.assertTrue(self.p1.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p1.tags['title'].value == 'Big Buck Bunny - test 1')
        self.assertTrue(self.p2.tags['comment'].value == 'Matroska Validation File 2, 100,000 timecode scale, odd aspect ratio, and CRC-32. Codecs are AVC and AAC')
        self.assertTrue(self.p2.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p2.tags['title'].value == 'Elephant Dream - test 2')
        self.assertTrue(self.p3.tags['comment'].value == 'Matroska Validation File 3, header stripping on the video track and no SimpleBlock')
        self.assertTrue(self.p3.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p3.tags['title'].value == 'Elephant Dream - test 3')
        #self.assertTrue(self.p4.tags['comment'].value == '')
        #self.assertTrue(self.p4.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        #self.assertTrue(self.p4.tags['title'].value == '')
        self.assertTrue(self.p5.tags['comment'].value == 'Matroska Validation File 8, secondary audio commentary track, misc subtitle tracks')
        self.assertTrue(self.p5.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p5.tags['title'].value == 'Big Buck Bunny - test 8')
        self.assertTrue(self.p6.tags['comment'].value == 'Matroska Validation File 6, random length to code the size of Clusters and Blocks, no Cues for seeking')
        self.assertTrue(self.p6.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p6.tags['title'].value == 'Big Buck Bunny - test 6')
        self.assertTrue(self.p7.tags['comment'].value == 'Matroska Validation File 7, junk elements are present at the beggining or end of clusters, the parser should skip it. There is also a damaged element at 451418')
        self.assertTrue(self.p7.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p7.tags['title'].value == 'Big Buck Bunny - test 7')
        self.assertTrue(self.p8.tags['comment'].value == 'Matroska Validation File 8, audio missing between timecodes 6.019s and 6.360s')
        self.assertTrue(self.p8.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p8.tags['title'].value == 'Big Buck Bunny - test 8')

    def test_video(self):
        self.assertTrue(self.p1.video[0].language == 'und')
        self.assertTrue(self.p1.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p1.video[0].codec == 'MP42')
        self.assertTrue(self.p1.video[0].width == 854)
        self.assertTrue(self.p1.video[0].height == 480)
        self.assertTrue(self.p1.video[0].fps == 24.000000384000003)
        self.assertTrue(self.p1.video[0].trackno == 1)
        self.assertTrue(self.p1.video[0].id == 0)
        
        self.assertTrue(self.p2.video[0].language == 'und')
        self.assertTrue(self.p2.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p2.video[0].codec == 'AVC1')
        self.assertTrue(self.p2.video[0].width == 1024)
        self.assertTrue(self.p2.video[0].height == 576)
        self.assertTrue(self.p2.video[0].fps == 24.000000960000037)
        self.assertTrue(self.p2.video[0].trackno == 1)
        self.assertTrue(self.p2.video[0].id == 0)
        
        self.assertTrue(self.p3.video[0].language == 'und')
        self.assertTrue(self.p3.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p3.video[0].codec == 'AVC1')
        self.assertTrue(self.p3.video[0].width == 1024)
        self.assertTrue(self.p3.video[0].height == 576)
        self.assertTrue(self.p3.video[0].fps == 24.000000960000037)
        self.assertTrue(self.p3.video[0].trackno == 1)
        self.assertTrue(self.p3.video[0].id == 0)
        
        self.assertTrue(self.p5.video[0].language == 'und')
        self.assertTrue(self.p5.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p5.video[0].codec == 'AVC1')
        self.assertTrue(self.p5.video[0].width == 1024)
        self.assertTrue(self.p5.video[0].height == 576)
        self.assertTrue(self.p5.video[0].fps == 24.000000960000037)
        self.assertTrue(self.p5.video[0].aspect == 1.7777777777777777)
        self.assertTrue(self.p5.video[0].trackno == 1)
        self.assertTrue(self.p5.video[0].id == 0)
        
        self.assertTrue(self.p6.video[0].language == 'und')
        self.assertTrue(self.p6.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p6.video[0].codec == 'MP42')
        self.assertTrue(self.p6.video[0].width == 854)
        self.assertTrue(self.p6.video[0].height == 480)
        self.assertTrue(self.p6.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p6.video[0].trackno == 1)
        self.assertTrue(self.p6.video[0].id == 0)
        self.assertTrue(self.p6.video[0].default == False)
        
        self.assertTrue(self.p7.video[0].language == 'und')
        self.assertTrue(self.p7.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p7.video[0].codec == 'AVC1')
        self.assertTrue(self.p7.video[0].width == 1024)
        self.assertTrue(self.p7.video[0].height == 576)
        self.assertTrue(self.p7.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p7.video[0].trackno == 1)
        self.assertTrue(self.p7.video[0].id == 0)
        self.assertTrue(self.p7.video[0].default == False)
        
        self.assertTrue(self.p8.video[0].language == 'und')
        self.assertTrue(self.p8.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p8.video[0].codec == 'AVC1')
        self.assertTrue(self.p8.video[0].width == 1024)
        self.assertTrue(self.p8.video[0].height == 576)
        self.assertTrue(self.p8.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p8.video[0].trackno == 1)
        self.assertTrue(self.p8.video[0].id == 0)
        self.assertTrue(self.p8.video[0].default == False)

    def test_audio(self):
        self.assertTrue(self.p1.audio[0].language == 'und')
        self.assertTrue(self.p1.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p1.audio[0].channels == 2)
        self.assertTrue(self.p1.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p1.audio[0].codec == 85)
        self.assertTrue(self.p1.audio[0].trackno == 2)
        self.assertTrue(self.p1.audio[0].id == 0)
        
        self.assertTrue(self.p2.audio[0].language == 'und')
        self.assertTrue(self.p2.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p2.audio[0].channels == 2)
        self.assertTrue(self.p2.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p2.audio[0].codec == 255)
        self.assertTrue(self.p2.audio[0].trackno == 2)
        self.assertTrue(self.p2.audio[0].id == 0)
        
        self.assertTrue(self.p3.audio[0].language == 'eng')
        self.assertTrue(self.p3.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p3.audio[0].channels == 2)
        self.assertTrue(self.p3.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p3.audio[0].codec == 85)
        self.assertTrue(self.p3.audio[0].trackno == 2)
        self.assertTrue(self.p3.audio[0].id == 0)
        
        self.assertTrue(self.p5.audio[0].language == 'und')
        self.assertTrue(self.p5.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p5.audio[0].channels == 2)
        self.assertTrue(self.p5.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p5.audio[0].codec == 255)
        self.assertTrue(self.p5.audio[0].trackno == 2)
        self.assertTrue(self.p5.audio[0].id == 0)
        self.assertTrue(self.p5.audio[1].language == 'eng')
        self.assertTrue(self.p5.audio[1].title == 'Commentary')
        self.assertTrue(self.p5.audio[1].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p5.audio[1].samplerate == 22050.0)
        self.assertTrue(self.p5.audio[1].codec == 255)
        self.assertTrue(self.p5.audio[1].trackno == 10)
        self.assertTrue(self.p5.audio[1].id == 1)
        
        self.assertTrue(self.p6.video[0].language == 'und')
        self.assertTrue(self.p6.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p6.video[0].codec == 'MP42')
        self.assertTrue(self.p6.video[0].width == 854)
        self.assertTrue(self.p6.video[0].height == 480)
        self.assertTrue(self.p6.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p6.video[0].trackno == 1)
        self.assertTrue(self.p6.video[0].id == 0)
        self.assertTrue(self.p6.video[0].default == False)
        
        self.assertTrue(self.p7.video[0].language == 'und')
        self.assertTrue(self.p7.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p7.video[0].codec == 'AVC1')
        self.assertTrue(self.p7.video[0].width == 1024)
        self.assertTrue(self.p7.video[0].height == 576)
        self.assertTrue(self.p7.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p7.video[0].trackno == 1)
        self.assertTrue(self.p7.video[0].id == 0)
        self.assertTrue(self.p7.video[0].default == False)
        
        self.assertTrue(self.p8.video[0].language == 'und')
        self.assertTrue(self.p8.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p8.video[0].codec == 'AVC1')
        self.assertTrue(self.p8.video[0].width == 1024)
        self.assertTrue(self.p8.video[0].height == 576)
        self.assertTrue(self.p8.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p8.video[0].trackno == 1)
        self.assertTrue(self.p8.video[0].id == 0)
        self.assertTrue(self.p8.video[0].default == False)

    def test_subtitles(self):
        self.assertTrue(len(self.p1.subtitles) == 0)
        self.assertTrue(len(self.p2.subtitles) == 0)
        self.assertTrue(len(self.p3.subtitles) == 0)
        self.assertTrue(self.p5.subtitles[0].language == 'eng')
        self.assertTrue(self.p5.subtitles[0].id == 0)
        self.assertTrue(self.p5.subtitles[0].trackno == 3)
        self.assertTrue(self.p5.subtitles[0].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[1].language == 'hun')
        self.assertTrue(self.p5.subtitles[1].id == 1)
        self.assertTrue(self.p5.subtitles[1].trackno == 4)
        self.assertTrue(self.p5.subtitles[1].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[2].language == 'ger')
        self.assertTrue(self.p5.subtitles[2].id == 2)
        self.assertTrue(self.p5.subtitles[2].trackno == 5)
        self.assertTrue(self.p5.subtitles[2].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[3].language == 'fre')
        self.assertTrue(self.p5.subtitles[3].id == 3)
        self.assertTrue(self.p5.subtitles[3].trackno == 6)
        self.assertTrue(self.p5.subtitles[3].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[4].language == 'spa')
        self.assertTrue(self.p5.subtitles[4].id == 4)
        self.assertTrue(self.p5.subtitles[4].trackno == 8)
        self.assertTrue(self.p5.subtitles[4].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[5].language == 'ita')
        self.assertTrue(self.p5.subtitles[5].id == 5)
        self.assertTrue(self.p5.subtitles[5].trackno == 9)
        self.assertTrue(self.p5.subtitles[5].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[6].language == 'jpn')
        self.assertTrue(self.p5.subtitles[6].id == 6)
        self.assertTrue(self.p5.subtitles[6].trackno == 11)
        self.assertTrue(self.p5.subtitles[6].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[7].language == 'und')
        self.assertTrue(self.p5.subtitles[7].id == 7)
        self.assertTrue(self.p5.subtitles[7].trackno == 7)
        self.assertTrue(self.p5.subtitles[7].codec == 'S_TEXT/UTF8')
        self.assertTrue(len(self.p6.subtitles) == 0)
        self.assertTrue(len(self.p7.subtitles) == 0)
        self.assertTrue(len(self.p8.subtitles) == 0)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(map(MKVTestCase, MKVTestCase.tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
