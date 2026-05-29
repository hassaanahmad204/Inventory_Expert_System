# knowledge_base.py

class Rule:
    def __init__(self, rule_id, category, conditions, conclusion, certainty, explanation):
        self.rule_id = rule_id
        self.category = category
        self.conditions = conditions  # Lambda function evaluating the facts dictionary
        self.conclusion = conclusion  # Dictionary of new facts to assert
        self.certainty = certainty    # Advanced Feature: Certainty Factor (0.0 to 1.0)
        self.explanation = explanation

def get_inventory_knowledge_base():
    rules = []

    # ==========================================
    # LAYER 1: DEMAND VELOCITY RULES (R01 - R20)
    # ==========================================
    rules.append(Rule("R01", "Demand", lambda f: f.get('recent_sales') > 150, {'demand_velocity': 'High'}, 0.95, "Recent sales volume is exceptionally high (over 150 units)."))
    rules.append(Rule("R02", "Demand", lambda f: 50 <= f.get('recent_sales') <= 150, {'demand_velocity': 'Medium'}, 0.90, "Recent sales volume is steady and moderate (50-150 units)."))
    rules.append(Rule("R03", "Demand", lambda f: f.get('recent_sales') < 50, {'demand_velocity': 'Low'}, 0.90, "Recent sales volume is weak (under 50 units)."))
    rules.append(Rule("R04", "Demand", lambda f: f.get('seasonality') == 'Peak Season' and f.get('demand_velocity') == 'High', {'anticipated_demand': 'Explosive'}, 0.85, "High baseline demand during a peak market season indicates explosive upcoming demand."))
    rules.append(Rule("R05", "Demand", lambda f: f.get('seasonality') == 'Off-Season' and f.get('demand_velocity') == 'Low', {'anticipated_demand': 'Stagnant'}, 0.80, "Low baseline demand during an off-season suggests stagnant market movement."))
    rules.append(Rule("R06", "Demand", lambda f: f.get('market_trend') == 'Trending Up', {'demand_trend_factor': 'Positive'}, 0.75, "External market analytical indicators are pointing upwards."))
    rules.append(Rule("R07", "Demand", lambda f: f.get('market_trend') == 'Trending Down', {'demand_trend_factor': 'Negative'}, 0.75, "External market analytical indicators suggest declining product interest."))
    rules.append(Rule("R08", "Demand", lambda f: f.get('demand_velocity') == 'High' and f.get('demand_trend_factor') == 'Positive', {'anticipated_demand': 'Explosive'}, 0.90, "High velocity backed by positive market trends confirms explosive demand scaling."))
    rules.append(Rule("R09", "Demand", lambda f: f.get('demand_velocity') == 'Medium' and f.get('demand_trend_factor') == 'Positive', {'anticipated_demand': 'High'}, 0.80, "Moderate velocity transitioning upward due to positive market trends."))
    rules.append(Rule("R10", "Demand", lambda f: f.get('demand_velocity') == 'Low' and f.get('demand_trend_factor') == 'Negative', {'anticipated_demand': 'Stagnant'}, 0.95, "Low baseline velocity worsening under declining market trends."))
    rules.append(Rule("R11", "Demand", lambda f: f.get('seasonality') == 'Peak Season' and f.get('demand_velocity') == 'Medium', {'anticipated_demand': 'High'}, 0.85, "Moderate sales entering peak season indicates elevated demand expectations."))
    rules.append(Rule("R12", "Demand", lambda f: f.get('seasonality') == 'Off-Season' and f.get('demand_velocity') == 'High', {'anticipated_demand': 'Medium'}, 0.75, "High baseline sales but entering an off-season trends toward moderate demand leveling."))
    rules.append(Rule("R13", "Demand", lambda f: f.get('seasonality') == 'Normal Season' and f.get('demand_velocity') == 'High', {'anticipated_demand': 'High'}, 0.90, "Consistent high performance during regular operational seasons indicates high demand stability."))
    rules.append(Rule("R14", "Demand", lambda f: f.get('seasonality') == 'Normal Season' and f.get('demand_velocity') == 'Medium', {'anticipated_demand': 'Medium'}, 0.90, "Steady mid-tier sales volume during standard seasons suggests predictable medium demand."))
    rules.append(Rule("R15", "Demand", lambda f: f.get('seasonality') == 'Normal Season' and f.get('demand_velocity') == 'Low', {'anticipated_demand': 'Low'}, 0.85, "Sluggish performance in a standard season confirms basic low demand requirements."))
    rules.append(Rule("R16", "Demand", lambda f: f.get('market_trend') == 'Stable' and f.get('demand_velocity') == 'Medium', {'anticipated_demand': 'Medium'}, 0.95, "A completely stable market trend paired with intermediate sales maps to steady standard demand forecasts."))
    rules.append(Rule("R17", "Demand", lambda f: f.get('market_trend') == 'Stable' and f.get('demand_velocity') == 'High', {'anticipated_demand': 'High'}, 0.90, "High velocity sales in a steady market environment reflect robust, ongoing demand."))
    rules.append(Rule("R18", "Demand", lambda f: f.get('market_trend') == 'Stable' and f.get('demand_velocity') == 'Low', {'anticipated_demand': 'Low'}, 0.90, "Low sales activity in a static, non-trending market indicates fixed weak demand paths."))
    rules.append(Rule("R19", "Demand", lambda f: f.get('seasonality') == 'Peak Season' and f.get('market_trend') == 'Trending Up', {'anticipated_demand': 'Explosive'}, 0.90, "The combination of high season calendars and organic upward user interest indicates sudden high traffic demand spikes."))
    rules.append(Rule("R20", "Demand", lambda f: f.get('seasonality') == 'Off-Season' and f.get('market_trend') == 'Trending Down', {'anticipated_demand': 'Stagnant'}, 0.95, "Entering seasonal dead zones alongside falling market popularity marks the product as structurally dormant."))

    # ==========================================
    # LAYER 2: SUPPLY LINE & RISK RULES (R21 - R38)
    # ==========================================
    rules.append(Rule("R21", "Supply", lambda f: f.get('supplier_lead_time') > 14, {'lead_time_category': 'Extended'}, 0.90, "Supplier fulfillment timeline takes longer than 2 weeks."))
    rules.append(Rule("R22", "Supply", lambda f: 5 <= f.get('supplier_lead_time') <= 14, {'lead_time_category': 'Standard'}, 0.90, "Supplier fulfillment timeline falls within normal parameters (5-14 days)."))
    rules.append(Rule("R23", "Supply", lambda f: f.get('supplier_lead_time') < 5, {'lead_time_category': 'Rapid'}, 0.95, "Supplier offers express dispatch (under 5 days)."))
    rules.append(Rule("R24", "Supply", lambda f: f.get('supplier_reliability') < 70, {'supply_risk': 'Critical'}, 0.85, "Supplier contract fulfillment reliability rate is unacceptably low (under 70%)."))
    rules.append(Rule("R25", "Supply", lambda f: 70 <= f.get('supplier_reliability') <= 85, {'supply_risk': 'Moderate'}, 0.80, "Supplier demonstrates average fulfillment consistency."))
    rules.append(Rule("R26", "Supply", lambda f: f.get('supplier_reliability') > 85, {'supply_risk': 'Negligible'}, 0.90, "Supplier possesses an elite track record for timely delivery."))
    rules.append(Rule("R27", "Supply", lambda f: f.get('lead_time_category') == 'Extended' and f.get('supply_risk') == 'Critical', {'supply_line_status': 'Highly Volatile'}, 0.95, "Long lead times compounded by an unreliable supplier creates extreme supply vulnerability."))
    rules.append(Rule("R28", "Supply", lambda f: f.get('lead_time_category') == 'Extended' and f.get('supply_risk') == 'Moderate', {'supply_line_status': 'Delayed'}, 0.80, "Long lead times with an average supplier will reliably delay arrivals."))
    rules.append(Rule("R29", "Supply", lambda f: f.get('lead_time_category') == 'Rapid' and f.get('supply_risk') == 'Negligible', {'supply_line_status': 'Highly Secure'}, 0.95, "Fast lead times and premium supplier reliability guarantees warehouse resilience."))
    rules.append(Rule("R30", "Supply", lambda f: f.get('geopolitical_disruption') == True, {'supply_risk': 'Critical'}, 0.90, "Active regional logistical borders or custom blockages are confirmed."))
    rules.append(Rule("R31", "Supply", lambda f: f.get('geopolitical_disruption') == True and f.get('lead_time_category') == 'Extended', {'supply_line_status': 'Highly Volatile'}, 0.95, "Active geopolitical blockages on top of an already long delivery window paralyzes the pipeline."))
    rules.append(Rule("R32", "Supply", lambda f: f.get('lead_time_category') == 'Standard' and f.get('supply_risk') == 'Negligible', {'supply_line_status': 'Highly Secure'}, 0.85, "Standard turnarounds managed by an elite supplier results in a highly secure pipeline."))
    rules.append(Rule("R33", "Supply", lambda f: f.get('lead_time_category') == 'Rapid' and f.get('supply_risk') == 'Moderate', {'supply_line_status': 'Standard Operational'}, 0.80, "Express dispatch capabilities balanced out by fluctuating supplier fulfillment rates."))
    rules.append(Rule("R34", "Supply", lambda f: f.get('lead_time_category') == 'Standard' and f.get('supply_risk') == 'Moderate', {'supply_line_status': 'Standard Operational'}, 0.85, "Normal turnaround expectations matched with normal supplier behavior profiles."))
    rules.append(Rule("R35", "Supply", lambda f: f.get('lead_time_category') == 'Rapid' and f.get('supply_risk') == 'Critical', {'supply_line_status': 'Highly Volatile'}, 0.75, "Fast delivery promises are negated by the supplier's critical failure rates."))
    rules.append(Rule("R36", "Supply", lambda f: f.get('geopolitical_disruption') == True and f.get('supply_risk') == 'Critical', {'supply_line_status': 'Paralyzed'}, 0.98, "Border blockages layered over completely failing supplier metrics points to an unusable logistics line."))
    rules.append(Rule("R37", "Supply", lambda f: f.get('lead_time_category') == 'Extended' and f.get('supply_risk') == 'Negligible', {'supply_line_status': 'Slow But Stable'}, 0.90, "Long transit delays are expected, but the trustworthy supplier eliminates delivery uncertainty."))
    rules.append(Rule("R38", "Supply", lambda f: f.get('geopolitical_disruption') == False and f.get('supply_risk') == 'Negligible', {'supply_line_status': 'Highly Secure'}, 0.90, "Clear logistics borders combined with an elite supplier establishes an optimal supply route."))

    # ==========================================
    # LAYER 3: WAREHOUSE CAPABILITY RULES (R39 - R55)
    # ==========================================
    rules.append(Rule("R39", "Storage", lambda f: f.get('current_stock') <= f.get('safety_stock_limit'), {'stock_status': 'Critically Low'}, 0.95, "Current physical stock has breached or met the established safety defense cushion."))
    rules.append(Rule("R40", "Storage", lambda f: f.get('safety_stock_limit') < f.get('current_stock') <= (f.get('safety_stock_limit') * 2), {'stock_status': 'Low'}, 0.85, "Stock levels are hovering slightly above safety limits; attention required."))
    rules.append(Rule("R41", "Storage", lambda f: (f.get('safety_stock_limit') * 2) < f.get('current_stock') <= (f.get('safety_stock_limit') * 3), {'stock_status': 'Moderate'}, 0.90, "Stock levels are safely resting in standard, non-threatening operational buffer zones."))
    rules.append(Rule("R42", "Storage", lambda f: f.get('current_stock') > (f.get('safety_stock_limit') * 3), {'stock_status': 'Surplus'}, 0.90, "Warehouse holding quantities significantly exceed operational safety buffers."))
    rules.append(Rule("R43", "Storage", lambda f: f.get('is_perishable') == True and f.get('days_to_expiration') <= 7, {'perishability_risk': 'Extreme'}, 0.95, "Perishable items are within a single week of spoiling."))
    rules.append(Rule("R44", "Storage", lambda f: f.get('is_perishable') == True and 7 < f.get('days_to_expiration') <= 30, {'perishability_risk': 'Moderate'}, 0.80, "Perishable items face expiration issues within the month."))
    rules.append(Rule("R45", "Storage", lambda f: f.get('is_perishable') == True and f.get('days_to_expiration') > 30, {'perishability_risk': 'Negligible'}, 0.90, "Perishable classification is active, but remaining shelf life leaves a safe time window."))
    rules.append(Rule("R46", "Storage", lambda f: f.get('storage_capacity_utilized') >= 90, {'warehouse_vacancy': 'Full'}, 0.95, "Warehouse capacity utilization is near maximum limits (90%+)."))
    rules.append(Rule("R47", "Storage", lambda f: f.get('storage_capacity_utilized') < 50, {'warehouse_vacancy': 'Abundant'}, 0.85, "More than half of the assigned storage racks are sitting vacant."))
    rules.append(Rule("R48", "Storage", lambda f: 50 <= f.get('storage_capacity_utilized') < 90, {'warehouse_vacancy': 'Balanced'}, 0.90, "Warehouse floor deployment parameters show sound, functional spatial distribution."))
    rules.append(Rule("R49", "Storage", lambda f: f.get('holding_cost_rate') == 'High' and f.get('stock_status') == 'Surplus', {'financial_drain': 'Severe'}, 0.85, "Excessive inventory volumes tied down in high-cost premium storage spaces."))
    rules.append(Rule("R50", "Storage", lambda f: f.get('holding_cost_rate') == 'Low' and f.get('stock_status') == 'Surplus', {'financial_drain': 'Mild'}, 0.75, "Surplus exists but low handling fees mitigate immediate economic damage."))
    rules.append(Rule("R51", "Storage", lambda f: f.get('stock_status') == 'Critically Low' and f.get('is_essential_item') == True, {'operational_threat': 'High'}, 0.95, "A core baseline revenue-generating product line faces immediate depletion threat."))
    rules.append(Rule("R52", "Storage", lambda f: f.get('perishability_risk') == 'Extreme' and f.get('stock_status') == 'Surplus', {'operational_threat': 'Spoilage Waste'}, 0.90, "Large quantities of overstocked inventory are actively expiring."))
    rules.append(Rule("R53", "Storage", lambda f: f.get('stock_status') == 'Low' and f.get('is_essential_item') == True, {'operational_threat': 'Medium'}, 0.85, "An essential item line is dipping down towards safety margins."))
    rules.append(Rule("R54", "Storage", lambda f: f.get('holding_cost_rate') == 'High' and f.get('storage_capacity_utilized') >= 90, {'financial_drain': 'Severe'}, 0.90, "A completely full warehouse operating under maximum carrying rates imposes severe structural financial overhead."))
    rules.append(Rule("R55", "Storage", lambda f: f.get('stock_status') == 'Critically Low' and f.get('is_essential_item') == False, {'operational_threat': 'Negligible'}, 0.80, "Non-essential inventory items are running completely dry, posing no threat to core business functionality."))

    # ==========================================
    # LAYER 4: REPLENISHMENT ACTION INFERENCE (R56 - R75)
    # ==========================================
    rules.append(Rule("R56", "Action", lambda f: f.get('stock_status') == 'Critically Low' and f.get('anticipated_demand') == 'Explosive' and f.get('supply_line_status') == 'Highly Secure', {'action': 'Emergency Express Bulk Order', 'priority_level': 'CRITICAL'}, 0.98, "Explosive demand colliding with critical low stock requires massive emergency ordering via safe supply pipelines."))
    rules.append(Rule("R57", "Action", lambda f: f.get('stock_status') == 'Critically Low' and f.get('supply_line_status') == 'Highly Volatile', {'action': 'Split-Source Expedited Ordering', 'priority_level': 'CRITICAL'}, 0.90, "Stock is critical but primary pipeline is blocked; immediately distribute secondary local purchase orders."))
    rules.append(Rule("R58", "Action", lambda f: f.get('stock_status') == 'Critically Low' and f.get('anticipated_demand') == 'Stagnant', {'action': 'Minimal Restock Order', 'priority_level': 'Medium'}, 0.75, "Stock is low, but market data reveals flat consumer interest. Restock to bare minimum levels only."))
    rules.append(Rule("R59", "Action", lambda f: f.get('stock_status') == 'Low' and f.get('anticipated_demand') == 'High', {'action': 'Standard Routine Reorder', 'priority_level': 'High'}, 0.85, "Standard operational signal triggered to return inventory to optimal thresholds under good demand."))
    rules.append(Rule("R60", "Action", lambda f: f.get('stock_status') == 'Low' and f.get('supply_line_status') == 'Delayed', {'action': 'Buffer-Inflated Advance Order', 'priority_level': 'High'}, 0.80, "Stock is low and supplier pipelines are lagging; order early and increase order volume to offset future lag."))
    rules.append(Rule("R61", "Action", lambda f: f.get('stock_status') == 'Surplus' and f.get('financial_drain') == 'Severe', {'action': 'Halt Ordering & Dynamic Markdown', 'priority_level': 'Low'}, 0.85, "Stop all procurement immediately; deploy aggressive promotional pricing to clear active financial overhead."))
    rules.append(Rule("R62", "Action", lambda f: f.get('operational_threat') == 'Spoilage Waste', {'action': 'Flash Liquidation Sale', 'priority_level': 'High'}, 0.95, "Stock is on the verge of total physical spoilage; drop prices immediately to salvage invested capital."))
    rules.append(Rule("R63", "Action", lambda f: f.get('warehouse_vacancy') == 'Full' and f.get('stock_status') != 'Critically Low', {'action': 'Freeze Active Procurement', 'priority_level': 'Low'}, 0.90, "Physical space limits reached; completely freeze non-essential inventory incoming streams."))
    rules.append(Rule("R64", "Action", lambda f: f.get('stock_status') == 'Surplus' and f.get('anticipated_demand') == 'Explosive', {'action': 'Hold Procurement (Asset Leveraging)', 'priority_level': 'Low'}, 0.80, "No new ordering required; current overstock perfectly positions us to capitalize on immediate demand surges."))
    rules.append(Rule("R65", "Action", lambda f: f.get('action') == 'Standard Routine Reorder' and f.get('warehouse_vacancy') == 'Abundant', {'action': 'Economic Order Quantity (EOQ) Bulk Order', 'priority_level': 'Medium'}, 0.85, "Abundant space permits moving from routine orders to high-volume bulk discounts using warehouse optimization models."))
    rules.append(Rule("R66", "Action", lambda f: f.get('stock_status') == 'Low' and f.get('warehouse_vacancy') == 'Full', {'action': 'Just-In-Time (JIT) Micro-Ordering', 'priority_level': 'Medium'}, 0.80, "Stock needs replenishment but the facility is gridlocked; order small micro-batches matching immediate delivery windows."))
    rules.append(Rule("R67", "Action", lambda f: f.get('operational_threat') == 'High' and f.get('supply_line_status') == 'Highly Secure', {'action': 'Priority Express Procurement', 'priority_level': 'CRITICAL'}, 0.95, "An essential asset is critically exposed. Order immediately via premium rapid logistics tracks."))
    rules.append(Rule("R68", "Action", lambda f: f.get('stock_status') == 'Moderate' and f.get('anticipated_demand') == 'High', {'action': 'Preemptive Small Batch Restock', 'priority_level': 'Medium'}, 0.80, "Current volumes are fine, but incoming sales indicators imply a small preventative order is optimal."))
    rules.append(Rule("R69", "Action", lambda f: f.get('stock_status') == 'Moderate' and f.get('anticipated_demand') == 'Medium', {'action': 'No Action Required (Maintain State)', 'priority_level': 'Routine'}, 0.95, "Perfect alignment across stock levels and pipeline demand fields."))
    rules.append(Rule("R70", "Action", lambda f: f.get('stock_status') == 'Moderate' and f.get('anticipated_demand') == 'Low', {'action': 'Monitor Stock (Defer Reorder)', 'priority_level': 'Routine'}, 0.85, "Inventory is stable but demand is softening; skip regular replenishment windows to track performance."))
    rules.append(Rule("R71", "Action", lambda f: f.get('stock_status') == 'Low' and f.get('anticipated_demand') == 'Stagnant', {'action': 'Strategic Tactical Deferral', 'priority_level': 'Low'}, 0.70, "Stock drops below average benchmarks, but completely stagnant market demand alerts management to freeze ordering strings."))
    rules.append(Rule("R72", "Action", lambda f: f.get('stock_status') == 'Surplus' and f.get('anticipated_demand') == 'Stagnant' and f.get('financial_drain') == 'Mild', {'action': 'Freeze Procurement & Monitor Velocity', 'priority_level': 'Low'}, 0.80, "High volume coupled with static consumer traffic requires a total pipeline freeze, though carrying costs are low enough to defer heavy price drops."))
    rules.append(Rule("R73", "Action", lambda f: f.get('supply_line_status') == 'Paralyzed' and f.get('stock_status') == 'Low', {'action': 'Force-Route Alternative Sourcing', 'priority_level': 'CRITICAL'}, 0.95, "The primary supply channel is completely broken and stocks are low; force an immediate shift to unverified local backup providers."))
    rules.append(Rule("R74", "Action", lambda f: f.get('supply_line_status') == 'Slow But Stable' and f.get('stock_status') == 'Low', {'action': 'Early Lifecycle Reorder Placements', 'priority_level': 'High'}, 0.85, "The transit pipeline is exceptionally slow but trustworthy; trigger a larger order early to accommodate extended timelines."))
    rules.append(Rule("R75", "Action", lambda f: f.get('stock_status') == 'Critically Low' and f.get('operational_threat') == 'Negligible', {'action': 'Low Priority Routine Restock', 'priority_level': 'Low'}, 0.80, "Non-essential stock has depleted completely; request a minor low-priority replenishment batch during standard ordering intervals."))

    # Conflict Resolution Strategy: Sort explicitly by Rule ID string to guarantee stable, predictable firing agendas
    rules.sort(key=lambda r: r.rule_id)
    return rules