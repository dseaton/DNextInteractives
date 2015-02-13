
# coding: utf-8

# In[43]:

get_ipython().run_cell_magic(u'HTML', u'', u'\n<div style="width: 100%; overflow: hidden;">\n            <div id=\'jxgbox1\' class=\'jxgbox\' style=\'width:350px; height:300px; float:left; border: solid #1f628d 2px;\'></div>        \n            <div id=\'jxgbox2\' class=\'jxgbox\' style=\'width:350px; height:300px; margin-left: 375px; border: solid #1f628d 2px;\'></div>\n        </div>\n\n        <!-- TURNED OFF\n        <input class="btn" type="button" value="Shift in Aggregate Demand" onClick="startAnimation()">\n        <input class="btn" type="button" value="Reset" onClick="resetAnimation()">\n        -->\n        \n        \n        <!-- COMMENT: Where our Javascript begins. -->\n        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>\n        \n        <!-- COMMENT: Specific Davidson Next calls built on JSXGraph. Must be loaded after JSXgraph. -->\n        <script type="text/javascript" src="../../../JS/Macro_JSXgraph.js"></script>\n        \n        <script type=\'text/javascript\'>\n            \n            \n            ////////////\n            // BOARD 1\n            ////////////\n            bboxlimits = [-1.5, 12, 12, -1];\n            var brd1 = JXG.JSXGraph.initBoard(\'jxgbox1\', {axis:true, \n                                                    showCopyright: false,\n                                                    showNavigation: false,\n                                                    zoom: false,\n                                                    pan: false,\n                                                    boundingbox:bboxlimits,\n                                                    grid: true,\n                                                    hasMouseUp: true, \n            });\n            \n            \n            ////////////\n            // BOARD 2\n            ////////////\n            bboxlimits2 = [-2.0, 12, 12, -1];\n            var brd2 = JXG.JSXGraph.initBoard(\'jxgbox2\', {axis:true, \n                                                    showCopyright: false,\n                                                    showNavigation: false,\n                                                    zoom: false,\n                                                    pan: false,\n                                                    boundingbox:bboxlimits2,\n                                                    grid: true,\n                                                    hasMouseUp: true, \n            });\n\n            \n            \n            \n            //Points\n            //var pointB1a = brd1.create(\'point\',[2,2])\n            \n            //Transform for shifting SRPC2\n            //var shift = brd1.create(\'transform\', [function(){return pointB1a.X()},\n            //                                      function(){return pointB1a.Y()}], {type:\'translate\'});\n            \n            //var pointB1b = brd1.create(\'point\',[pointB1a,shift])\n            //brd1.update()\n        \n            var Acoords = [1,1];\n            var A = brd1.create(\'point\', Acoords, {name:\'A\', style:5});\n            \n            var Bcoords = [8,8];\n            var shiftB = brd2.create(\'transform\', Bcoords, {type:\'translate\'});\n            var B = brd1.create(\'point\',[A,shiftB],{name:\'B\'});\n            var S = brd1.create(\'segment\',[A,B],{fixed:false,strokeWidth:3});\n            brd1.update();\n            \n            //////////\n            // Connect Boards and Movement\n            //////////\n            brd1.addChild(brd2);\n    \n            //var shiftC = brd2.create(\'transform\', [0,8], {type:\'translate\'});\n            //var C = brd2.create(\'point\',[A,shiftC],{name:\'C\'});\n            //var shiftD = brd2.create(\'transform\', [8,0], {type:\'translate\'});\n            //var D = brd2.create(\'point\',[A,shiftD],{name:\'D\'});\n            \n            var theLine = brd2.create(\'line\',[[10,0],[10,12]],{dash:1});\n            var reflectBrd2 = brd2.create(\'transform\',[theLine],{type:\'reflect\'});\n            var shiftC = brd2.create(\'transform\',[10,0],{type:\'translate\'});\n            var C = brd2.create(\'point\',[B,[shiftC,reflectBrd2]],{name:\'C\'});\n            \n            var shiftD = brd2.create(\'transform\',[10,0],{type:\'translate\'});\n            var D = brd2.create(\'point\',[A,[shiftD,reflectBrd2]],{name:\'D\'});\n            var E = brd2.create(\'segment\',[C,D],{fixed:false,strokeWidth:3});\n            \n            //var shift = brd1.create(\'transform\', [function(){return pointB1a.X()},\n            //                                      function(){return pointB1a.Y()}], {type:\'translate\'});\n            \n            //brd2.zoomAllPoints();\n            brd2.update(); \n            \n            \n            \n        </script>\n    </body>\n</html>')


# In[67]:

import re

#tmpfile = _i86
index_htmlinput = [ i for i,x in enumerate(_ih) if "run_cell_magic(u'HTML'" in x and "re.sub('%%HTML','',tmpfile)" not in x]

tmpfile = eval('_i%d' % int(index_htmlinput[-1]))
tmpfile = re.sub('%%HTML','',tmpfile)
tmpfile = re.sub(r'<!--START-BUTTON FOR PASS STATE(.*?)END-BUTTON FOR PASS STATE-->','',tmpfile,flags=re.DOTALL)
tmpfile = re.sub(r'//START-PASS STATE TO IPYTHON KERNEL(.*?)//END-PASS STATE TO IPYTHON KERNEL','',tmpfile,flags=re.DOTALL)

filename = 'testTransform'
html_filename = '%s.html' % filename

with open(html_filename,'w') as hfile:
    hfile.write(tmpfile)
print tmpfile


# In[ ]:



