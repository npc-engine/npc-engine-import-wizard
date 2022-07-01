# NPC Engine Import Wizard CLI

Python CLI tool for converting models into npc-engine server format.

## Installation

You can install it via pip. Import wizards might have their own extra requirements.

e.g.
```
pip install npc-engine-import-wizard[transformers]
```

## Usage

You can use the CLI tool to convert models from popular libraries into npc-engine services.

To start the wizard, run the following command:

```
npc-engine-import-wizard import --models-path <path-to-models> <model-path-or-id>
```

It will prompt you to select the import wizard for the model. 
Each service has its own set of import wizards for each library.   
It will also omit import wizards that lack their extras installed 
(i.e. with `npc-engine-import-wizard[transformers]` you will only see 
import wizards for [transformers](https://huggingface.co/docs/transformers/main/en/index) library).

e.g. 
```
