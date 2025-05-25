
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

    if (!node._isRestoring) {
      node._dynamicInputs = new Set();
    }
  
    const removeUnusedInputs = () => {
      for (let i = node.inputs.length - 1; i >= 0; i--) {
        const input = node.inputs[i];
        const isDynamic = node._dynamicInputs?.has(input.name);
  
        if (input.link || (isDynamic && node._isRestoring)) {
          continue;
        }
  
        if (isDynamic) {
          node.removeInput(i);
          node._dynamicInputs.delete(input.name);
        }
      }
    };
  
    const prevRestoring = node._isRestoring;
    if (node._isRestoring) {
      node._dynamicInputs = new Set(
        node.inputs
          .filter((input) => input.name.startsWith(connectionPrefix))
          .map((input) => input.name)
      );
    }
  
    removeUnusedInputs();
  
    const lastInput = node.inputs[node.inputs.length - 1];
    if (lastInput?.link && !node._isRestoring) {
      const newIndex = node.inputs.length + 1;
      const newName = `${connectionPrefix}${newIndex}`;
      const newInput = node.addInput(newName, connectionType);
      node._dynamicInputs.add(newName);
    }
  
    let validIndex = 1;
    node.inputs.forEach((input) => {
      if (input.name.startsWith(connectionPrefix)) {
        input.name = `${connectionPrefix}${validIndex++}`;
        input.label = input.name;
      }
    });
    node._isRestoring = prevRestoring;
}

export const log = (...args) => {
    console.debug(...args)
  }