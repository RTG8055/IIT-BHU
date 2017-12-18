graph [
  directed 1
  node [
    id 0
    label "0"
    cc 0
    cs 1.0
    bc 1
  ]
  node [
    id 1
    label "1"
    cc 1
    bc 1
  ]
  node [
    id 2
    label "2"
    cc 1
    cs 1.0
    bc 0
  ]
  node [
    id 3
    label "3"
    cc 0
    cs 0.0
    bc 0
  ]
  node [
    id 4
    label "4"
    cc 0
    cs 2.0
    bc 2
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 0
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 2
    target 1
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 3
    target 2
  ]
  edge [
    source 4
    target 1
  ]
  edge [
    source 4
    target 2
  ]
]
