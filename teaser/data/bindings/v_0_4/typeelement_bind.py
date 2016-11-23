# .\typeelement_bind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:19ffe95f3b2b26427defccbb12bc477d74a55bde
# Generated 2016-10-14 14:56:05.128811 by PyXB version 1.2.4 using Python 3.5.2.final.0
# Namespace http://teaser.elements

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:913c023a-920d-11e6-8efb-2cd444b2e704')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://teaser.elements', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# List simple type: {http://teaser.elements}integerList
# superclasses pyxb.binding.datatypes.anySimpleType
class integerList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerList')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 117, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.integer
integerList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerList', integerList)

# Complex type {http://teaser.elements}layerType with content type ELEMENT_ONLY
class layerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}layerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'layerType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpteaser_elements_layerType_httpteaser_elementsid', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 7, 6), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://teaser.elements}thickness uses Python identifier thickness
    __thickness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'thickness'), 'thickness', '__httpteaser_elements_layerType_httpteaser_elementsthickness', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 8, 6), )

    
    thickness = property(__thickness.value, __thickness.set, None, None)

    
    # Element {http://teaser.elements}material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'material'), 'material', '__httpteaser_elements_layerType_httpteaser_elementsmaterial', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 9, 6), )

    
    material = property(__material.value, __material.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __thickness.name() : __thickness,
        __material.name() : __material
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'layerType', layerType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute material_id uses Python identifier material_id
    __material_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'material_id'), 'material_id', '__httpteaser_elements_CTD_ANON_material_id', pyxb.binding.datatypes.string)
    __material_id._DeclarationLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 13, 5)
    __material_id._UseLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 13, 5)
    
    material_id = property(__material_id.value, __material_id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __material_id.name() : __material_id
    })



# Complex type {http://teaser.elements}LayersType with content type ELEMENT_ONLY
class LayersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}LayersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LayersType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 20, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}layer uses Python identifier layer
    __layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'layer'), 'layer', '__httpteaser_elements_LayersType_httpteaser_elementslayer', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 22, 6), )

    
    layer = property(__layer.value, __layer.set, None, None)

    _ElementMap.update({
        __layer.name() : __layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LayersType', LayersType)


# Complex type {http://teaser.elements}OuterWallType with content type ELEMENT_ONLY
class OuterWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}OuterWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OuterWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 25, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser_elements_OuterWallType_httpteaser_elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 27, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser.elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser_elements_OuterWallType_httpteaser_elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 28, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser.elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser_elements_OuterWallType_httpteaser_elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 29, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser.elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_elements_OuterWallType_httpteaser_elementsinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 30, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser.elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_elements_OuterWallType_httpteaser_elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 31, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser.elements}outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), 'outer_convection', '__httpteaser_elements_OuterWallType_httpteaser_elementsouter_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 32, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element {http://teaser.elements}outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser_elements_OuterWallType_httpteaser_elementsouter_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 33, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element {http://teaser.elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser_elements_OuterWallType_httpteaser_elementsLayers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 34, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OuterWallType', OuterWallType)


# Complex type {http://teaser.elements}InnerWallType with content type ELEMENT_ONLY
class InnerWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}InnerWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InnerWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 37, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser_elements_InnerWallType_httpteaser_elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 39, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser.elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser_elements_InnerWallType_httpteaser_elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 40, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser.elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser_elements_InnerWallType_httpteaser_elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 41, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser.elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_elements_InnerWallType_httpteaser_elementsinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 42, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser.elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_elements_InnerWallType_httpteaser_elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 43, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser.elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser_elements_InnerWallType_httpteaser_elementsLayers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 44, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InnerWallType', InnerWallType)


# Complex type {http://teaser.elements}RooftopType with content type ELEMENT_ONLY
class RooftopType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}RooftopType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RooftopType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 47, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser_elements_RooftopType_httpteaser_elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 49, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser.elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser_elements_RooftopType_httpteaser_elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 50, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser.elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser_elements_RooftopType_httpteaser_elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 51, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser.elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_elements_RooftopType_httpteaser_elementsinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 52, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser.elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_elements_RooftopType_httpteaser_elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 53, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser.elements}outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), 'outer_convection', '__httpteaser_elements_RooftopType_httpteaser_elementsouter_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 54, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element {http://teaser.elements}outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser_elements_RooftopType_httpteaser_elementsouter_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 55, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element {http://teaser.elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser_elements_RooftopType_httpteaser_elementsLayers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 56, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RooftopType', RooftopType)


# Complex type {http://teaser.elements}GroundFloorType with content type ELEMENT_ONLY
class GroundFloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}GroundFloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundFloorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 59, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser_elements_GroundFloorType_httpteaser_elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 61, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser.elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser_elements_GroundFloorType_httpteaser_elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 62, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser.elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser_elements_GroundFloorType_httpteaser_elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 63, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser.elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_elements_GroundFloorType_httpteaser_elementsinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 64, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser.elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_elements_GroundFloorType_httpteaser_elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 65, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser.elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser_elements_GroundFloorType_httpteaser_elementsLayers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 66, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GroundFloorType', GroundFloorType)


# Complex type {http://teaser.elements}WindowType with content type ELEMENT_ONLY
class WindowType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}WindowType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindowType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser_elements_WindowType_httpteaser_elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 71, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser.elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser_elements_WindowType_httpteaser_elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 72, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser.elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser_elements_WindowType_httpteaser_elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 73, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser.elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_elements_WindowType_httpteaser_elementsinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 74, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser.elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_elements_WindowType_httpteaser_elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 75, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser.elements}outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), 'outer_convection', '__httpteaser_elements_WindowType_httpteaser_elementsouter_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 76, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element {http://teaser.elements}outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser_elements_WindowType_httpteaser_elementsouter_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 77, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element {http://teaser.elements}g_value uses Python identifier g_value
    __g_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'g_value'), 'g_value', '__httpteaser_elements_WindowType_httpteaser_elementsg_value', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 78, 6), )

    
    g_value = property(__g_value.value, __g_value.set, None, None)

    
    # Element {http://teaser.elements}a_conv uses Python identifier a_conv
    __a_conv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'a_conv'), 'a_conv', '__httpteaser_elements_WindowType_httpteaser_elementsa_conv', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 79, 6), )

    
    a_conv = property(__a_conv.value, __a_conv.set, None, None)

    
    # Element {http://teaser.elements}shading_g_total uses Python identifier shading_g_total
    __shading_g_total = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shading_g_total'), 'shading_g_total', '__httpteaser_elements_WindowType_httpteaser_elementsshading_g_total', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 80, 6), )

    
    shading_g_total = property(__shading_g_total.value, __shading_g_total.set, None, None)

    
    # Element {http://teaser.elements}shading_max_irr uses Python identifier shading_max_irr
    __shading_max_irr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shading_max_irr'), 'shading_max_irr', '__httpteaser_elements_WindowType_httpteaser_elementsshading_max_irr', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 81, 6), )

    
    shading_max_irr = property(__shading_max_irr.value, __shading_max_irr.set, None, None)

    
    # Element {http://teaser.elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser_elements_WindowType_httpteaser_elementsLayers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 82, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __g_value.name() : __g_value,
        __a_conv.name() : __a_conv,
        __shading_g_total.name() : __shading_g_total,
        __shading_max_irr.name() : __shading_max_irr,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WindowType', WindowType)


# Complex type {http://teaser.elements}CeilingType with content type ELEMENT_ONLY
class CeilingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}CeilingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CeilingType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 85, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser_elements_CeilingType_httpteaser_elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 87, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser.elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser_elements_CeilingType_httpteaser_elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 88, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser.elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser_elements_CeilingType_httpteaser_elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 89, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser.elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_elements_CeilingType_httpteaser_elementsinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 90, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser.elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_elements_CeilingType_httpteaser_elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 91, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser.elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser_elements_CeilingType_httpteaser_elementsLayers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 92, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CeilingType', CeilingType)


# Complex type {http://teaser.elements}FloorType with content type ELEMENT_ONLY
class FloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}FloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FloorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 95, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser_elements_FloorType_httpteaser_elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 97, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser.elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser_elements_FloorType_httpteaser_elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 98, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser.elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser_elements_FloorType_httpteaser_elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 99, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser.elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_elements_FloorType_httpteaser_elementsinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 100, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser.elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_elements_FloorType_httpteaser_elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 101, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser.elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser_elements_FloorType_httpteaser_elementsLayers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 102, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FloorType', FloorType)


# Complex type {http://teaser.elements}TypeBuildingElementsType with content type ELEMENT_ONLY
class TypeBuildingElementsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.elements}TypeBuildingElementsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeBuildingElementsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 105, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.elements}OuterWall uses Python identifier OuterWall
    __OuterWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OuterWall'), 'OuterWall', '__httpteaser_elements_TypeBuildingElementsType_httpteaser_elementsOuterWall', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 108, 6), )

    
    OuterWall = property(__OuterWall.value, __OuterWall.set, None, None)

    
    # Element {http://teaser.elements}InnerWall uses Python identifier InnerWall
    __InnerWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InnerWall'), 'InnerWall', '__httpteaser_elements_TypeBuildingElementsType_httpteaser_elementsInnerWall', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 109, 6), )

    
    InnerWall = property(__InnerWall.value, __InnerWall.set, None, None)

    
    # Element {http://teaser.elements}Rooftop uses Python identifier Rooftop
    __Rooftop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rooftop'), 'Rooftop', '__httpteaser_elements_TypeBuildingElementsType_httpteaser_elementsRooftop', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 110, 6), )

    
    Rooftop = property(__Rooftop.value, __Rooftop.set, None, None)

    
    # Element {http://teaser.elements}GroundFloor uses Python identifier GroundFloor
    __GroundFloor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GroundFloor'), 'GroundFloor', '__httpteaser_elements_TypeBuildingElementsType_httpteaser_elementsGroundFloor', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 111, 6), )

    
    GroundFloor = property(__GroundFloor.value, __GroundFloor.set, None, None)

    
    # Element {http://teaser.elements}Window uses Python identifier Window
    __Window = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Window'), 'Window', '__httpteaser_elements_TypeBuildingElementsType_httpteaser_elementsWindow', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 112, 6), )

    
    Window = property(__Window.value, __Window.set, None, None)

    
    # Element {http://teaser.elements}Ceiling uses Python identifier Ceiling
    __Ceiling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ceiling'), 'Ceiling', '__httpteaser_elements_TypeBuildingElementsType_httpteaser_elementsCeiling', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 113, 6), )

    
    Ceiling = property(__Ceiling.value, __Ceiling.set, None, None)

    
    # Element {http://teaser.elements}Floor uses Python identifier Floor
    __Floor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Floor'), 'Floor', '__httpteaser_elements_TypeBuildingElementsType_httpteaser_elementsFloor', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 114, 6), )

    
    Floor = property(__Floor.value, __Floor.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpteaser_elements_TypeBuildingElementsType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 106, 1)
    __version._UseLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 106, 1)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __OuterWall.name() : __OuterWall,
        __InnerWall.name() : __InnerWall,
        __Rooftop.name() : __Rooftop,
        __GroundFloor.name() : __GroundFloor,
        __Window.name() : __Window,
        __Ceiling.name() : __Ceiling,
        __Floor.name() : __Floor
    })
    _AttributeMap.update({
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', 'TypeBuildingElementsType', TypeBuildingElementsType)


TypeBuildingElements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TypeBuildingElements'), TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', TypeBuildingElements.name().localName(), TypeBuildingElements)



layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.int, scope=layerType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 7, 6)))

layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thickness'), pyxb.binding.datatypes.float, scope=layerType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 8, 6)))

layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'material'), CTD_ANON, scope=layerType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 9, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 7, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'thickness')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 8, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'material')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 9, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
layerType._Automaton = _BuildAutomaton()




LayersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'layer'), layerType, scope=LayersType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 22, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 22, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LayersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'layer')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 22, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LayersType._Automaton = _BuildAutomaton_()




OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 27, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 28, 3)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 29, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 30, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 31, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 32, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 33, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 34, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 27, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 27, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 28, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 29, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 30, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 31, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 32, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 33, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 34, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OuterWallType._Automaton = _BuildAutomaton_2()




InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 39, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 40, 3)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 41, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 42, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 43, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 44, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 39, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 39, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 41, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 42, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 43, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 44, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InnerWallType._Automaton = _BuildAutomaton_3()




RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 49, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 50, 3)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 51, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 52, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 53, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 54, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 55, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 56, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 49, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 49, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 50, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 51, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 52, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 53, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 54, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 55, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 56, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RooftopType._Automaton = _BuildAutomaton_4()




GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 61, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 62, 3)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 63, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 64, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 65, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 66, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 61, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 61, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 62, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 63, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 64, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 65, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 66, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GroundFloorType._Automaton = _BuildAutomaton_5()




WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 71, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 72, 3)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 73, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 74, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 75, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 76, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 77, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'g_value'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 78, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'a_conv'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 79, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shading_g_total'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 80, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shading_max_irr'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 81, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 82, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 71, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 71, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 72, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 73, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 74, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 75, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 76, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 77, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'g_value')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 78, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'a_conv')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 79, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shading_g_total')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 80, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shading_max_irr')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 81, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 82, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WindowType._Automaton = _BuildAutomaton_6()




CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 87, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 88, 3)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 89, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 90, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 91, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 92, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 87, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 87, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 88, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 89, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 90, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 91, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 92, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CeilingType._Automaton = _BuildAutomaton_7()




FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 97, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 98, 3)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 99, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 100, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 101, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 102, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 97, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 98, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 99, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 100, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 101, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 102, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FloorType._Automaton = _BuildAutomaton_8()




TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OuterWall'), OuterWallType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 108, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InnerWall'), InnerWallType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 109, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rooftop'), RooftopType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 110, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroundFloor'), GroundFloorType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 111, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Window'), WindowType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 112, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ceiling'), CeilingType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 113, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Floor'), FloorType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 114, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 107, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OuterWall')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 108, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InnerWall')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 109, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rooftop')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 110, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GroundFloor')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 111, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Window')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 112, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ceiling')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 113, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Floor')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 114, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TypeBuildingElementsType._Automaton = _BuildAutomaton_9()

