import {app } from "../../scripts/app.js";
import { log, dynamic_connection, findWidgetByName, toggleWidget } from './utils.js'

app.registerExtension({
	name: "TextTranslation.text",

	async beforeRegisterNodeDef(nodeType, nodeData, app) {

		switch(nodeData.name){
			case 'Text_Concatenate':
				text_concatenate_widget(nodeType, nodeData, app);
			break;

			case 'Text_Translation_V2':	
			case 'Text_Translation_V2_Full':	
				text_translation_v2_widget(nodeType, nodeData, app);
			break;
		}
	},
});

function text_concatenate_widget(nodeType, nodeData, app) {
	var input_name = "text";

	const onNodeCreated = nodeType.prototype.onNodeCreated;
	nodeType.prototype.onNodeCreated = function () {
		const onc = onNodeCreated?.apply(this, arguments);
		this.addInput(`${input_name}1`, "STRING");
		return onc;
	};

	const onConnectionsChange = nodeType.prototype.onConnectionsChange;
	nodeType.prototype.onConnectionsChange = function (type, index, connected, link_info) {
		if(!link_info)
			return;

		const occ = onConnectionsChange
		? onConnectionsChange.apply(this, arguments)
		: undefined

		// log("输入类型：" +this.inputs[0].type);
		dynamic_connection(this, index, connected, input_name, this.inputs[0].type );
	  return occ
	}
}

function text_translation_v2_widget(nodeType, nodeData, app) {
	const onNodeCreated = nodeType.prototype.onNodeCreated;
			nodeType.prototype.onNodeCreated = function () {
				const onc = onNodeCreated?.apply(this, arguments);
			
				let node = this;

				toggleWidget(node, findWidgetByName(node, 'translator'), false);
				toggleWidget(node, findWidgetByName(node, 'source_language'), false);
				toggleWidget(node, findWidgetByName(node, 'target_language'), false);

				node.addWidget("button", "Show / Hide button", "button_show", function(value, widget, node){

					let is_show = null 
					if(this.value === "button_show") {
						is_show = true;
					} else if (this.value === "button_hide") {
						is_show = false;
					}

					toggleWidget(node, findWidgetByName(node, 'translator'), is_show)
					toggleWidget(node, findWidgetByName(node, 'source_language'), is_show)
					toggleWidget(node, findWidgetByName(node, 'target_language'), is_show)
					this.value = is_show ? "button_hide" : "button_show";
					app.graph.setDirtyCanvas(true);

				 });
				return onc;
			};

}

