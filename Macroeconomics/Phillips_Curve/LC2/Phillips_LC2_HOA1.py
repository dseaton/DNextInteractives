# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ### Phillips Curve - LC1, Hands-On Activity 1
# 
# Useful links:
# 
# Pi Symbol:  http://www.intmath.com/cg3/jsxgraph-axes-ticks-grids.php

# <codecell>

%%HTML

<!DOCTYPE html>
<html>
    <head>
        <style> 
            body {
                margin: 10px;
                /*padding-top: 40px;*/
            }
        </style>
    </head>

    <body>
        <!-- COMMENT: Define the jxgbox - aka, where all the interactive graphing will go. -->
        <div style="width: 100%; overflow: hidden;">
            <div id='jxgbox1' class='jxgbox' style='width:450px; height:350px; float:left; border: solid #1f628d 2px;'></div>
        </div>
        
        
        <!--START-BUTTON FOR PASS STATE-->
        <!-- COMMENT: Buttons below are used to add debugging features to an interactive. Conole logging allows you to see
            output within a browser's console. Try reading about Chrome's console. -->
        
        <input class="btn" type="button" value="Pass State for Grading" onClick="passState()">
        <div id="spaceBelow">State:</div>
        <!--END-BUTTON FOR PASS STATE-->
        
        <input class="btn" type="button" value="Increase in Inflationary Expectations" onClick="increaseInfExpect()">
        <input class="btn" type="button" value="Increase in Key Input Price" onClick="increaseKeyInputPrice()">
        <input class="btn" type="button" value="Increase in Labor Productivity" onClick="increaseLaborProd()">
        <input class="btn" type="button" value="Reset" onClick="resetAnimation()">
        
        <!-- COMMENT: Where our Javascript begins. -->
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>
        <script type='text/javascript'>

            bboxlimits = [-1.1, 12, 12, -1.1];
            var board = JXG.JSXGraph.initBoard('jxgbox1', {axis:false, 
                                                    showCopyright: false,
                                                    showNavigation: false,
                                                    zoom: false,
                                                    pan: false,
                                                    boundingbox:bboxlimits,
                                                    grid: false,
                                                    hasMouseUp: true, 
            });
            
            xaxis = board.create('axis', [[0, 0], [12, 0]], {withLabel: true, name: "Real GDP", label: {offset: [320,-20]}});
            yaxis = board.create('axis', [[0, 0], [0, 12]], {withLabel: true, name: "Price Level", label: {offset: [-60,260]}});

            //Axes
            xaxis.removeAllTicks();
            yaxis.removeAllTicks();
            var xlabel = board.create('text',[-0.65,10,"\u03c0"],{fixed:true,fontsize:20});
            var ylabel = board.create('text',[9,-0.5,"UR"],{fixed:true,fontsize:18});
            
            //Define Segments
            var xi1 = 2.0
            var yi1 = 10.0
            var xi2 = 10.0
            var yi2 = 2.0
            var f1 = board.create('point',[xi1,yi1],{withLabel:false,visible:false});
            var f2 = board.create('point',[xi2,yi2],{withLabel:false,visible:false});
            
            //SRPC1
            var SRPC1 = board.create('segment',[f1,f2],{strokeColor:'Gray',strokeWidth:'3',
                                                      name:'SRPC1',withLabel:true,dash:'1',
                                                      fixed:true,highlight:false,
                                                      label:{color:'Gray',highlight:false,offset:[125,-85]}});
            
            //SRPC2
            var S1 = board.create('point',[xi1,yi1],{withLabel:false,visible:false});
            var S2 = board.create('point',[xi2,yi2],{withLabel:false,visible:false});
            var SRPC2 = board.create('segment',[S1,S2],{strokeColor:'Blue',strokeWidth:'3',
                                                      name:'SRPC2',withLabel:false});
            
            board.on('mousedown', function() {      
                SRPC2.setAttribute({withLabel:true});
                board.update()
            });
            
            //Animation for Unknown Condition
            increaseLaborProd = function() {
                S1.moveTo([1.0,9.0],1000);
                S2.moveTo([9.0,1.0],1000);
                SRPC2.setAttribute({withLabel:true});                
                board.update();
            }
            
            //Animation for Inflationary Expectations
            increaseInfExpect = function() {
                S1.moveTo([3.0,11.0],1000);
                S2.moveTo([11.0,3.0],1000);
                SRPC2.setAttribute({withLabel:true});
                board.update();
            }
            
            //Animation for Increase in Key Input Price (same as Inf. Expectations)
            increaseKeyInputPrice = function() {
                S1.moveTo([3.0,11.0],1000);
                S2.moveTo([11.0,3.0],1000);
                SRPC2.setAttribute({withLabel:true});
                board.update();
            }
            
            resetAnimation = function() {
                S1.moveTo([2.0,10.0],10);
                S2.moveTo([10.0,2.0],10);
                board.update();
                SRPC2.setAttribute({withLabel:false});
            }
            
            //Grading Functions
            
            //START-PASS STATE TO IPYTHON KERNEL
            passState = function(){
                var state = {'f1':f1.getAttribute('strokeColor'),'f2':f2.getAttribute('strokeColor')};
                statestr = JSON.stringify(state);
                document.getElementById('spaceBelow').innerHTML += '<br>'+statestr;
                var command = "state = '" + statestr + "'";
                console.log(command);

                var kernel = IPython.notebook.kernel;
                kernel.execute(command);

                return statestr
            }
                
            //END-PASS STATE TO IPYTHON KERNEL
            
            //Standard edX JSinput functions
            getInput = function(){
                var state = {'f1':f1.getAttribute('strokeColor'),'f2':f2. getAttribute('strokeColor')};
                statestr = JSON.stringify(state);
                //console.log(statestr);
                return statestr;
            }

            getState = function(){
                state = JSON.parse(getInput());
                statestr = JSON.stringify(state);
                // console.log(statestr);
                return statestr;
            }

            setState = function(statestr){
                state = JSON.parse(statestr);

                if (state["f1"]) {
                    f1.setAttribute({strokeColor: state["f1"],strokeWidth: 4});
                    f2.setAttribute({strokeColor: state["f2"],strokeWidth: 4});
                    board.update();
                }
                //alert(statestr);
                console.debug('State updated successfully from saved.');
            }
            
        </script>
    </body>
</html>

# <markdowncell>

# ###Ungraded

# <codecell>

import re

#tmpfile = _i86
index_htmlinput = [ i for i,x in enumerate(_ih) if "run_cell_magic(u'HTML'" in x and "re.sub('%%HTML','',tmpfile)" not in x]

tmpfile = eval('_i%d' % int(index_htmlinput[-1]))
tmpfile = re.sub('%%HTML','',tmpfile)
tmpfile = re.sub(r'<!--START-BUTTON FOR PASS STATE(.*?)END-BUTTON FOR PASS STATE-->','',tmpfile,flags=re.DOTALL)
tmpfile = re.sub(r'//START-PASS STATE TO IPYTHON KERNEL(.*?)//END-PASS STATE TO IPYTHON KERNEL','',tmpfile,flags=re.DOTALL)

filename = 'Phillips_LC1_HOA1'
html_filename = '%s.html' % filename

with open(html_filename,'w') as hfile:
    hfile.write(tmpfile)
print tmpfile

# <codecell>


