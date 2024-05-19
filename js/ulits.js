
export const isPropertiesWidgetShow = (widget_name) => {
  if(properties_widget[widget_name]){
      return properties_widget[widget.name].value.includes('_hide');
  }else{
    return false;
  }
};


let origProps = {};
export const findWidgetByName = (node, name) => node.widgets.find((w) => w.name === name);

export const doesInputWithNameExist = (node, name) => node.inputs ? node.inputs.some((input) => input.name === name) : false;

export function updateNodeHeight(node) {node.setSize([node.size[0], node.computeSize()[1]]);}

export function toggleWidget(node, widget, show = false, suffix = "") {
	if (!widget || doesInputWithNameExist(node, widget.name)) return;
	if (!origProps[widget.name]) {
		origProps[widget.name] = { origType: widget.type, origComputeSize: widget.computeSize };
	}
	const origSize = node.size;

	widget.type = show ? origProps[widget.name].origType : "easyHidden" + suffix;
	widget.computeSize = show ? origProps[widget.name].origComputeSize : () => [0, -4];

	widget.linkedWidgets?.forEach(w => toggleWidget(node, w, ":" + widget.name, show));

	const height = show ? Math.max(node.computeSize()[1], origSize[1]) : node.size[1];
	node.setSize([node.size[0], height]);
}


export const dynamic_connection = (
	node,
	index,
	connected,
	connectionPrefix = 'input_',
	connectionType = 'PSDLAYER'
  ) => {

	if (!connected && (node.inputs.length > 1)) {
        const stackTrace = new Error().stack;
        for (let i =  0; i < node.inputs.length -1; i++) {
            if(!stackTrace.includes('LGraphNode.prototype.connect') &&
            !stackTrace.includes('LGraphNode.connect') &&
            !stackTrace.includes('loadGraphData') &&
            !node.inputs[i].link) {
                    node.removeInput(i);
                }
        }
    }

    let last_slot = node.inputs[node.inputs.length - 1];
    if (last_slot.link != undefined) {
        node.addInput(`${connectionPrefix}`, connectionType);
    }

    if (connected && (node.inputs.length > 1)) {
        const stackTrace = new Error().stack;
        for (let i =  0; i < node.inputs.length -1; i++) {
            if(!stackTrace.includes('LGraphNode.prototype.connect') &&
            !stackTrace.includes('LGraphNode.connect') &&
            !stackTrace.includes('loadGraphData') &&
            !node.inputs[i].link) {
                    node.removeInput(i);
                }
        }
    }

	if ((node.inputs.length > 1)) {
		for (let i =  0; i < node.inputs.length -1; i++) {
			node.inputs[i].name = `${connectionPrefix}${i + 1}`
			node.inputs[i].label = `${connectionPrefix}${i + 1}`
		}
    }
}

export const log = (...args) => {
    console.debug(...args)
  }