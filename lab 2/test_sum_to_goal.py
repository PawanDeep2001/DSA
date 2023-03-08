#
#   Author: Catherine Leung
#   Timing for fibonacci
#   To use this, run: python test_sum_to_goal.py
#


import unittest
from lab1 import sum_to_goal

class SumToGoalTestCase(unittest.TestCase):
    """These are the test cases for sum_to_goal, runned 20 times to get timing"""
    

    def test_sum_to_goal(self):
        mylist =[658091, 869492, 329197, 442502, 886040, 763872, 586122, 833571,719591, 563368, 
         681304, 103894, 430560, 825535, 371591, 78470, 687013, 571497, 478056, 904017, 
         688375, 2925, 878786, 781874, 541594, 378502, 961485, 87957, 23350, 592897, 461990, 
         629123, 842857, 325329, 620217, 804160, 439546, 499690, 844158, 365299, 313190, 450884, 
         250584, 208273, 885831, 978509, 100206, 910602, 986182, 29507, 627916, 902412, 660549, 
         894525, 735297, 132991, 256814, 464847, 665083, 945362, 211068, 131959, 255045, 430114, 
         783252, 873386, 296287, 893729, 251919, 45532, 97639, 114562, 158077, 490883, 202998, 504727, 
         470212, 305295, 3876, 527938, 688505, 448578, 713166, 377572, 151093, 884757, 985142, 92336, 
         374010, 431786, 711826, 604537, 63851, 523593, 314817, 879344, 346752, 698204, 299249, 999289, 
         155035, 90399, 6173, 613175, 819672, 15125, 464794, 807477, 779540, 971324, 359406, 44889, 
         198376, 557879, 188722, 476722, 923238, 970512, 57467, 439574, 42271, 100988, 336810, 636603, 
         993885, 351372, 575455, 461822, 19264, 397599, 927424, 29356, 709299, 255851, 587083, 6107, 
         257020, 334360, 559063, 134747, 485538, 912504, 456016, 172023, 362967, 204382, 723388, 248523, 
         988123, 592718, 389608, 755799, 323045, 605408, 36052, 820356, 187316, 132742, 939735, 516992, 
         608412, 926420, 841160, 620969, 135554, 94396, 937001, 328507, 782584, 776703, 513784, 993349, 
         676036, 972639, 32658, 119365, 24414, 228669, 546375, 766306, 638767, 719839, 254496, 616576, 
         606747, 857720, 251751, 35551, 709340, 299436, 534988, 70415, 563075, 157435, 293160, 33325, 
         99895, 412961, 201260, 772365, 188208, 434006, 783949, 859438, 317665, 988407, 337774, 370707, 
         263991, 441658, 506474, 504532, 682031, 668329, 899194, 732473, 358153, 324214, 340178, 97490, 117259, 
         906670, 225520, 398954, 936560, 114684, 942651, 362220, 532394, 927771, 916999, 487498, 812889, 273008, 
         486820, 977872, 128966, 455422, 879770, 94767, 836709, 74577, 435341, 986878, 864217, 636799, 305850, 
         128739, 251337, 159142, 508012, 938405, 148860, 547159, 858571, 145800, 538325, 611389, 316178, 67368, 
         536708, 423586, 13864, 155626, 759670, 174913, 461750, 255120, 403991, 122740, 849297, 454397, 613437, 
         300202, 944117, 79905, 250037, 355222, 475690, 386046, 171861, 580684, 675237, 554709, 907802, 749609, 
         750037, 577519, 845800, 958832, 506670, 34637, 575786, 438906, 909138, 494947, 280506, 251050, 630450, 
         471012, 284367, 590935, 126711, 936012, 572501, 829316, 128731, 629229, 498037, 722177, 506452, 935840, 
         61504, 211408, 880500, 619328, 404400, 962390, 534921, 318099, 694351, 923673, 938787, 190551, 964596, 
         634650, 801067, 563202, 609430, 108211, 443836, 991492, 776372, 624915, 413814, 85605, 33662, 722983, 
         255512, 575204, 383971, 16032, 235058, 497171, 620144, 305483, 274961, 907843, 875085, 894961, 512005, 
         464270, 908670, 626077, 44250, 756629, 287790, 255127, 825074, 597935, 972151, 115370, 62876, 74973, 
         225687, 392570, 483130, 827928, 590805, 696723, 675822, 967649, 292267, 754624, 102697, 38692, 428419, 
         796934, 905216, 52553, 930135, 557583, 366650, 456436, 11869, 773883, 277901, 895614, 378808, 82818, 
         111104, 443656, 220426, 160574, 646445, 171271, 637564, 611051, 760549, 663186, 352984, 852063, 164367, 
         720802, 439918, 142378, 98011, 479943, 830106, 850386, 858991, 246319, 317273, 522517, 672811, 855828,
          733860, 398381, 640662, 536205, 681152, 576468, 835533, 929608, 82807, 201113, 979117, 405422, 826304, 
          648840, 387130, 373101, 629599, 534069, 207000, 992901, 45998, 3682, 122583, 592675, 220928, 964838, 
          213402, 749722, 605907, 993783, 527222, 127079, 560627, 251775, 986973, 429473, 464047, 695142, 742357, 
          312002, 119179, 962251, 256912, 396706, 717512, 833286, 148660, 899393, 57187, 209327, 462866, 816111, 
          850930, 688334, 753225, 490811, 9641, 76631, 254894, 524165, 699224, 79971, 898028, 170512, 949085, 
          572113, 445327, 372848, 433148, 599800, 746762, 251802, 632657, 368188, 759861, 887506, 175643, 452952, 
          797986, 123233, 894654, 702901, 404096, 24640, 243837, 921655, 943398, 157879, 913382, 800555, 788971, 
          927438, 911566, 761410, 364114, 283890, 83456, 875735, 770697, 385498, 620686, 583558, 406687, 63325, 
          428119, 539838, 809161, 966989, 877536, 728760, 403551, 570684, 878449, 547700, 44785, 795440, 872493, 
          515708, 535078, 664087, 217116, 697857, 632881, 248905, 572851, 348621, 408387, 147445, 654512, 687497,
          922878, 210762, 341967, 929559, 893916, 150970, 813394, 759124, 840419, 555757, 241207, 946780, 706472, 
          651403, 748491, 613152, 540833, 324920, 693150, 351515, 611202, 833925, 44218, 359333, 118241, 103393, 
          318518, 231676, 927814, 688117, 834509, 115893, 252025, 64133, 473313, 886596, 715349, 459102, 262153, 
          932142, 720793, 650849, 55098, 831264, 595250, 58020, 158792, 198545, 752085, 888952, 217322, 50070, 
          643431, 595440, 997596, 177162, 501064, 730371, 565289, 173031, 445313, 220832, 561868, 376985, 340256, 
          803780, 187019, 871631, 623004, 272229, 656950, 673782, 195318, 126777, 584114, 818085, 312190, 640050, 
          559625, 940791, 157932, 651826, 350885, 267664, 551536, 133765, 263492, 21836, 103443, 891242, 360031, 
          121559, 710303, 23823, 653401, 673523, 621696, 310049, 594569, 502312, 509303, 685987, 196795, 974818, 
          882050, 808448, 390965, 801760, 211911, 98758, 314599, 633354, 975056, 795955, 721106, 226011, 206504, 
          607577, 905449, 252629, 294411, 506459, 862158, 768749, 336860, 42813, 780791, 221550, 198712, 506266, 
          619528, 707827, 981815, 599088, 5703, 72985, 173462, 431966, 785209, 983605, 915969, 683278, 470978, 
          809732, 320566, 33470, 277819, 57725, 32034, 431767, 7952, 855542, 31197, 904858, 532371, 907396, 582199, 
          680492, 437392, 906697, 918561, 156459, 494160, 686424, 839966, 18557, 987029, 161221, 351684, 432986, 
          76410, 79495, 602861, 165890, 272802, 198162, 63358, 364936, 480591, 788965, 811273, 151658, 348737, 
          246845, 813753, 415896, 18529, 76188, 308061, 741031, 434047, 165615, 578416, 208244, 835455, 647067, 
          310133, 786621, 531885, 943146, 469880, 189997, 573708, 420242, 57713, 609630, 933115, 715871, 361794, 
          522562, 191554, 843161, 598359, 633108, 46099, 396062, 51644, 651591, 231134, 374451, 28577, 894438, 
          941215, 445751, 453044, 230498, 14745, 625140, 393513, 672241, 991204, 696188, 573591, 115329, 367630, 
          556785, 989141, 514212, 563168, 902310, 15192, 973436, 360664, 352104, 682800, 9042, 113435, 647922, 
          344965, 618480, 48104, 111175, 393909, 462428, 64963, 303082, 420338, 885386, 52384, 791730, 663357, 
          144995, 344492, 68243, 74802, 774818, 205272, 568191, 266255, 719517, 41546, 266096, 144684, 870430, 
          757606, 986016, 714167, 846697, 536751, 92986, 695662, 410542, 12148, 459110, 232146, 27171, 600255, 
          3966, 127929, 598898, 760963, 727277, 407469, 26439, 800929, 992472, 70559, 33910, 982684, 777105, 
          900874, 71859, 982874, 809865, 598447, 578297, 513340, 643403, 395957, 302578, 745438, 300066, 145551, 
          877469, 38153, 782434, 609958, 30031, 102890, 895424, 866426, 767769, 369205, 674603, 120229, 688073, 
          967935, 606136, 554716, 734511, 400220, 150470, 371931, 774525, 310593, 591034, 451323, 914787, 180528, 
          498141, 885866, 863137, 534506, 697843, 36185, 630438, 144781, 195595, 373209, 605388, 507025, 526628, 
          220624, 153638, 186571, 104893, 355125, 867056, 508102, 88772, 401720, 78535, 122839, 857780, 507185, 
          529580, 215509, 511259, 775326, 384382, 343672, 594854, 262501, 664064, 702967, 93455, 876604, 699140, 
          413775, 584426, 822437, 656673, 777332, 793603, 840786, 823452, 35010, 987022, 746740, 707622, 772172, 
          995675, 883483, 343151, 285084, 879594, 499078, 612124, 447105, 215563, 351920, 605613, 669087, 162254, 
          70966, 851456, 987768, 442416, 627927, 921135, 834178, 666970, 390012, 231048, 493282, 999003, 186101, 
          834494, 370148, 254466, 594809, 232871, 81908, 704239, 673473, 576972, 202866, 940838, 493219, 878567, 
          692876, 253643, 183260, 656848, 7844, 80159, 115157, 548233, 295957, 523849, 861412, 899176, 762260, 
          230096, 264030, 755543, 203470, 223305, 117835, 334564, 508300, 687466, 936209, 824653]

        self.assertEqual(sum_to_goal(mylist,1377780),385241373216)
        self.assertEqual(sum_to_goal(mylist,1002212),151879073211)
        self.assertEqual(sum_to_goal(mylist,282071),8009685258)
        self.assertEqual(sum_to_goal(mylist,1110806),296025296920)
        self.assertEqual(sum_to_goal(mylist,1122540),194011867476)
        self.assertEqual(sum_to_goal(mylist,1377780),385241373216)
        self.assertEqual(sum_to_goal(mylist,1002212),151879073211)
        self.assertEqual(sum_to_goal(mylist,282071),8009685258)
        self.assertEqual(sum_to_goal(mylist,1110806),296025296920)
        self.assertEqual(sum_to_goal(mylist,1122540),194011867476)
        self.assertEqual(sum_to_goal(mylist,1377780),385241373216)
        self.assertEqual(sum_to_goal(mylist,1002212),151879073211)
        self.assertEqual(sum_to_goal(mylist,282071),8009685258)
        self.assertEqual(sum_to_goal(mylist,1110806),296025296920)
        self.assertEqual(sum_to_goal(mylist,1122540),194011867476)
        self.assertEqual(sum_to_goal(mylist,1377780),385241373216)
        self.assertEqual(sum_to_goal(mylist,1002212),151879073211)
        self.assertEqual(sum_to_goal(mylist,282071),8009685258)
        self.assertEqual(sum_to_goal(mylist,1110806),296025296920)
        self.assertEqual(sum_to_goal(mylist,1122540),194011867476)
        self.assertEqual(sum_to_goal(mylist,1377780),385241373216)
        self.assertEqual(sum_to_goal(mylist,1002212),151879073211)
        self.assertEqual(sum_to_goal(mylist,282071),8009685258)
        self.assertEqual(sum_to_goal(mylist,1110806),296025296920)
        self.assertEqual(sum_to_goal(mylist,1122540),194011867476)
   

if __name__ == '__main__':
    unittest.main()
