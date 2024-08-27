from lxml import etree
import spacy

nlp = spacy.load("en_core_web_sm")

def process_natural_language(policy_text):
    doc = nlp(policy_text)
    entities = {'subjects': [], 'actions': [], 'resources': [], 'conditions': []}
    
    for token in doc:
        if token.dep_ == "nsubj":
            entities['subjects'].append(token.text)
        elif token.dep_ == "ROOT":
            entities['actions'].append(token.text)
        elif token.dep_ == "dobj":
            entities['resources'].append(token.text)
        elif token.dep_ in ["advcl", "prep"]:
            entities['conditions'].append(token.text)
    
    xacml_policy = generate_xacml(entities)
    return {'entities': entities, 'xacml_policy': xacml_policy}

def generate_xacml(entities):
    policy = etree.Element("Policy")
    target = etree.SubElement(policy, "Target")
    
    subject = etree.SubElement(target, "Subject")
    subject.text = ', '.join(entities['subjects'])
    
    resource = etree.SubElement(target, "Resource")
    resource.text = ', '.join(entities['resources'])
    
    action = etree.SubElement(target, "Action")
    action.text = ', '.join(entities['actions'])
    
    condition = etree.SubElement(target, "Condition")
    condition.text = ', '.join(entities['conditions'])
    
    return etree.tostring(policy, pretty_print=True).decode()
