# inference_engine.py
from knowledge_base import get_inventory_knowledge_base

class InventoryInferenceEngine:
    def __init__(self):
        self.working_memory = {}
        self.knowledge_base = get_inventory_knowledge_base()
        self.fired_rules_log = []     # Tracks rule objects fired (Explanation Module)
        self.execution_steps = []     # Tracks reasoning log strings (Reasoning Visualization)

    def run_forward_chaining(self, initial_facts):
        """
        Executes standard Forward Chaining.
        Starts with basic facts, evaluates rule conditions, derives intermediate conclusions,
        and pushes forward until no more rules can fire.
        """
        self.working_memory = initial_facts.copy()
        self.fired_rules_log = []
        self.execution_steps = []
        
        agenda = list(self.knowledge_base)
        loop_control = True
        
        self.execution_steps.append(f"🟢 System Working Memory initialized with user context facts.")
        
        while loop_control:
            rule_fired_this_cycle = False
            
            for rule in agenda:
                # Conflict Resolution Safeguard: Ensure a rule never fires twice to prevent infinite loops
                if rule.rule_id in [r.rule_id for r in self.fired_rules_log]:
                    continue
                
                # Check if conditions evaluate to True within working memory
                if rule.conditions(self.working_memory):
                    # Fire Rule: Merge conclusion dictionary facts into working memory
                    self.working_memory.update(rule.conclusion)
                    self.fired_rules_log.append(rule)
                    
                    log_entry = (
                        f"🔥 RULE FIRED [{rule.rule_id}] ({rule.category}): {rule.explanation} "
                        f"-> Derived Conclusions: {rule.conclusion} (CF: {rule.certainty})"
                    )
                    self.execution_steps.append(log_entry)
                    
                    rule_fired_this_cycle = True
                    break  # Break loop to restart priority agenda verification from scratch (Conflict Resolution Strategy)
            
            if not rule_fired_this_cycle:
                loop_control = False  # No matching rules found; Inference has completed successfully
                
        self.execution_steps.append(f"🏁 Forward Chaining inference successfully terminated. Working memory stabilized.")
        return self.working_memory

    def get_explanation_data(self):
        """Returns ordered log of fired rules for the Explanation Module UI"""
        return self.fired_rules_log

    def get_execution_logs(self):
        """Returns step-by-step reasoning process visualization logs"""
        return self.execution_steps