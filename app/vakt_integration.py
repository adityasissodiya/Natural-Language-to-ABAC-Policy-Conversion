from vakt import Policy, Inquiry, ALLOW_ACCESS, Guard
from vakt.storage.memory import MemoryStorage
from vakt.rules import Eq
from vakt.checker import RulesChecker  # Import the required checker

def enforce_policy(entities):
    try:
        # Create a policy
        policy = Policy(
            1,
            subjects=[Eq(entities['subjects'][0])],
            actions=[Eq(entities['actions'][0])],
            resources=[Eq(entities['resources'][0])],
            context={'condition': Eq(entities['conditions'][0])}
        )

        # Store the policy
        storage = MemoryStorage()
        storage.add(policy)

        # Initialize the Guard with a RulesChecker
        guard = Guard(storage, RulesChecker())  # Add RulesChecker as the checker

        # Create an inquiry based on the entities
        inquiry = Inquiry(
            subject=entities['subjects'][0],
            action=entities['actions'][0],
            resource=entities['resources'][0],
            context={'condition': entities['conditions'][0]}
        )

        # Check if the inquiry is allowed based on the policy
        return "Access Granted" if guard.is_allowed(inquiry) else "Access Denied"
    except Exception as e:
        print(f"Error during policy enforcement: {e}")
        raise e
