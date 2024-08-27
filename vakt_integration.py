from vakt import Policy, Inquiry, ALLOW_ACCESS, Guard
from vakt.storage.memory import MemoryStorage
from vakt.rules import Eq

def enforce_policy(entities):
    policy = Policy(
        1,
        subjects=[Eq(entities['subjects'][0])],
        actions=[Eq(entities['actions'][0])],
        resources=[Eq(entities['resources'][0])],
        context={'condition': Eq(entities['conditions'][0])}
    )

    # Store and enforce policy
    storage = MemoryStorage()
    storage.add(policy)
    guard = Guard(storage)
    
    inquiry = Inquiry(
        subject=entities['subjects'][0],
        action=entities['actions'][0],
        resource=entities['resources'][0],
        context={'condition': entities['conditions'][0]}
    )
    
    return "Access Granted" if guard.is_allowed(inquiry) else "Access Denied"
