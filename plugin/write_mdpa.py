#  _  __         _          ___       _               ___ _           _
# | |/ /_ _ __ _| |_ ___ __/ __| __ _| |___ _ __  ___| _ \ |_  _ __ _(_)_ _
# | ' <| '_/ _` |  _/ _ (_-<__ \/ _` | / _ \ '  \/ -_)  _/ | || / _` | | ' \
# |_|\_\_| \__,_|\__\___/__/___/\__,_|_\___/_|_|_\___|_| |_|\_,_\__, |_|_||_|
#                                                               |___/
# License: BSD License ; see LICENSE
#
# Main authors: Philipp Bucher (https://github.com/philbucher)
#

import time

def _WriteHeaderMdpa(model_part, additional_header, file_stream):
    def WriteSubModelPartInfo(model_part,
                                file_stream,
                                level):
        SPACE = "    "
        for smp in model_part.SubModelParts:
            full_name = [smp.Name]
            psmp = smp
            while psmp.IsSubModelPart():
                psmp = psmp.GetParentModelPart()
                full_name.append(psmp.Name)
            file_stream.write("// " + SPACE*level + "SubModelPart " + ".".join(full_name[::-1]) + "\n")
            file_stream.write("// " + SPACE*level + "Number of Nodes: " + str(smp.NumberOfNodes()) + "\n")
            file_stream.write("// " + SPACE*level + "Number of Elements: " + str(smp.NumberOfElements()) + "\n")
            file_stream.write("// " + SPACE*level + "Number of Conditions: " + str(smp.NumberOfConditions()) + "\n")
            file_stream.write("// " + SPACE*level + "Number of SubModelParts: " + str(smp.NumberOfSubModelParts()) + "\n")
            WriteSubModelPartInfo(smp,file_stream, level+1)

    localtime = time.asctime( time.localtime(time.time()) )
    file_stream.write("// File created on " + localtime + "\n")
    file_stream.write("// Mesh Information:\n")
    file_stream.write("// Number of Nodes: " + str(model_part.NumberOfNodes()) + "\n")
    file_stream.write("// Number of Elements: " + str(model_part.NumberOfElements()) + "\n")
    file_stream.write("// Number of Conditions: " + str(model_part.NumberOfConditions()) + "\n")
    file_stream.write("// Number of SubModelParts: " + str(model_part.NumberOfSubModelParts()) + "\n")
    WriteSubModelPartInfo(model_part,file_stream, level=0)
    file_stream.write("\n")


def _WriteNodesMdpa(nodes, file_stream):
    file_stream.write("Begin Nodes\n")
    for node in nodes:
        file_stream.write('{} {} {} {}'.format(node.Id, node.X, node.Y, node.Z))
    file_stream.write("End Nodes\n\n")

def _WriteEntitiesMdpa(entities, entity_name, file_stream):
    file_stream.write("Begin {}s\n".format(entity_name))
    for entity in entities:
        file_stream.write('{} {} {} {}'.format(node.Id, node.X, node.Y, node.Z))
    file_stream.write("End {}s\n\n".format(entity_name))

def _WriteEntityDataMdpa(entities, entity_name, file_stream):
    pass

def _WriteSubModelPartMdpa(sub_model_part, file_stream, level=0):
    file_stream.write("{}Begin SubModelPart\n".format("\t"*level))

    # write SubModelParts recursively
    for smp in sub_model_part.SubModelParts:
        _WriteSubModelPartMdpa(smp, file_stream, level+1)
    file_stream.write("{}End SubModelPart\n".format("\t"*level))


def WriteMdpa(model_part, file_name, additional_header=""):
    if not file_name.endswith(".mdpa"):
        file_name += ".mdpa"

    with open(file_name, 'w') as mdpa_file:
        _WriteHeaderMdpa(model_part, additional_header, mdpa_file)

        _WriteNodesMdpa(model_part.Nodes, mdpa_file)
        _WriteEntitiesMdpa(model_part.Elements, "Element", mdpa_file)
        _WriteEntitiesMdpa(model_part.Conditions, "Condition", mdpa_file)

        _WriteEntityDataMdpa(model_part.Nodes, "Nod", mdpa_file)
        _WriteEntityDataMdpa(model_part.Elements, "Element", mdpa_file)
        _WriteEntityDataMdpa(model_part.Conditions, "Condition", mdpa_file)

        for smp in model_part.SubModelParts:
            _WriteSubModelPartMdpa(smp, mdpa_file)