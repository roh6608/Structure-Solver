# Structure-Solver
A command line interface application for solving structural mechanics problems.

# Getting Started

## Requirements

## Data Format
To get started the data will have to be formatted in the correct manner, for the nodes data the file has to be formatted as below.

```node,x,y```

Where node is the node number, x is the x coordinate of the node, and y is the y coordinate of the node. For the member data the file will have to be formatted as below.

```element,from,to```

Where element is the element number, from is the node from which the element starts, to is the node at which the element ends. For the external force data, the file will have to be formatted as shown below.

```node,magnitude,direction```

Where node is the location at which the external force is applied, magnitude is the magnitude of the force, the solver assumes this value is in kN and direction is the direction in which the force is acting. For the reaction data, the file will have to be formatted as shown below.

```num,node,direction```

Where num is an index number, node is the node that has a support reaction and direction is the direction in which there is a reaction.

## Options

## Examples

# Method

# Authors

# Licence
