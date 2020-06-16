<img width="2074" alt="SunFlow Image" src="https://user-images.githubusercontent.com/65338147/84592654-9392bd80-ae47-11ea-9712-a1f59069b32f.png">


# Design & Optimize your Supply Chain

SunFlow is a tool to model and optimize your Supply Chains. In SunFlow a model is made of materials, components, parts, products, substitutes, suppliers, manufactures, distributors and customers - just to mention the major ones - together with fix and variable costs, capacities and other constraints. 


Tutorials
---------

Illustrative tutorials explain SunFlow's capabilities and their usage by Python examples step-by-step. Their source code is inside the examples folder.


Powerful Graphics
-----------------

SunFlow got powerful graphics. Your network can be displayed at any time. Have a look on the artificial and schematic assembly of a Porsche Taycan electric as an example. First you graph the network with all potential connections and definitions for cost, freight, capacities, products, components, suppliers, plants, distribution centers and customers or markets.

<img width="930" alt="Taycan Graph" src="https://user-images.githubusercontent.com/65338147/84734869-63136680-afa2-11ea-9587-22faee26e7a3.png">

Once you got the network you execute the potential flows to identify the cost-optimal flow, i.e. you optimize it. Our optimized network is shown below.

<img width="991" alt="Taycan GraphOpt" src="https://user-images.githubusercontent.com/65338147/84734883-6a3a7480-afa2-11ea-90ff-f63ed025800f.png">

The optimized model show active (blue) and inactive flows (gray) as well as active participants (gray boxes) and inactive participants (white boxes). In complex models this could be confusing. Therefore you can show those vertices and edges only, which have an active flow (see below).

<img width="936" alt="TaycanGraphOptFlowOnly" src="https://user-images.githubusercontent.com/65338147/84734892-70c8ec00-afa2-11ea-857f-b9a4401522c5.png">


Network Compiler
----------------

SunFlow's Supply Networks are build up in a way Supply Chain Architects think: in terms of compoments, material, products, suppliers, plants, assambly lines, reactors, warehouses, distribution centers, customers, markets,...  The above shown illustrations are made by the Python example below.

<img width="978" alt="Taycan Code" src="https://user-images.githubusercontent.com/65338147/84736175-8ab7fe00-afa5-11ea-943e-5b16238f9f60.png">


Library
-------

The SunFlow library file 'sunflow.py' can be found in folder 'lib'. To add the library or import search path at load-time, the file 'aitpath.py' from 'lib' folder can be used after adaption to the your directory settings. Its usage is described in the examples.



Dependencies
------------

SunFlow supports Python 3.6+

The installation requires [numpy](http://www.numpy.org/), [scipy](http://www.scipy.org/), [pandas](http://pandas.pydata.org/) and [graphviz](https://www.graphviz.org).



Data
----

Some of the examples use data which can be found inside the folder 'data'.



Installation
------------

To install SunFlow on your computer, press 'Clone or download' on SunFlow's Repository site and choose the 'Download ZIP' option. Then SunFlow will be copied into a folder 'SunFlow' in your download directory, containing the complete repository. To proceed further, read the guide in the folder 'lib'.

