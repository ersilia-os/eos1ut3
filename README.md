# USR descriptors with pharmacophoric constraints

USRCAT is a real-time ultrafast molecular shape recognition with pharmacophoric constraints. It integrates atom type to the traditional Ultrafast Shape Recognition (USR) descriptor to improve the performance of shape-based virtual screening, being able to discriminate between compounds with similar shape but distinct pharmacophoric features.

This model was incorporated on 2023-11-28.Last packaged on 2026-03-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos1ut3`
- **Slug:** `molfeat-usrcat`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `60`
- **Output Consistency:** `Fixed`
- **Interpretation:** 60 features based on USRCAT

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_00 | float |  | USRCAT feature index 0 |
| feat_01 | float |  | USRCAT feature index 1 |
| feat_02 | float |  | USRCAT feature index 2 |
| feat_03 | float |  | USRCAT feature index 3 |
| feat_04 | float |  | USRCAT feature index 4 |
| feat_05 | float |  | USRCAT feature index 5 |
| feat_06 | float |  | USRCAT feature index 6 |
| feat_07 | float |  | USRCAT feature index 7 |
| feat_08 | float |  | USRCAT feature index 8 |
| feat_09 | float |  | USRCAT feature index 9 |

_10 of 60 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos1ut3](https://hub.docker.com/r/ersiliaos/eos1ut3)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1ut3.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1ut3.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `5676`
- **Image Size (Mb):** `7917.95`

**Computational Performance (seconds):**
- 10 inputs: `35.75`
- 100 inputs: `48.04`
- 10000 inputs: `1197.82`

### References
- **Source Code**: [https://molfeat.datamol.io/featurizers/usrcat](https://molfeat.datamol.io/featurizers/usrcat)
- **Publication**: [https://doi.org/10.1186/1758-2946-4-27](https://doi.org/10.1186/1758-2946-4-27)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2012`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos1ut3
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos1ut3
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
