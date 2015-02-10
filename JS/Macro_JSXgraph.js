//////////////////////////////////////////////////////////////////
// JSXgraph functions designed to help build Macro interactives.
//
// http://academics.davidson.edu/davidsonnext/
//
// http://jsxgraph.uni-bayreuth.de/wp/
//
//////////////////////////////////////////////////////////////////

//General Parameters for Macro
JXG.Options.point.showInfobox = false;
JXG.Options.segment.strokeColor = 'Pink';

createDragLine = function(board,point1,point2,gname,color,xo,yo) {
    return board.create('segment',[point1,point2],{strokeColor:color,strokeWidth:'3',name:gname,withLabel:true,label:{offset:[xo,yo]}});
}

createSupply = function(board,gname,color) {
    var c1 = [1.0,2.0];
    var c2 = [9.0,10.0];
    var S1 = board.create('point',c1,{withLabel:false,visible:false});
    var S2 = board.create('point',c2,{withLabel:false,visible:false});
    return board.create('segment',[S1,S2],{'strokeColor':color,'strokeWidth':'3',
                                           'name':gname,'withLabel':true,
                                           'label':{'offset':[105,105]}
                                          });
}

createDemand = function(board,gname,color) {
    var c1 = [1.0,10.0];
    var c2 = [9.0,2.0];
    var D1 = board.create('point',c1,{withLabel:false,visible:false});
    var D2 = board.create('point',c2,{withLabel:false,visible:false});
    return board.create('segment',[D1,D2],{'strokeColor':color,'strokeWidth':'3',
                                           'name':gname,'withLabel':true,
                                           'label':{'offset':[105,-105]}
                                          });
}
