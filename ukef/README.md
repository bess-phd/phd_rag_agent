# UKEF Agent - Knowledge Base Setup Guide

## 📋 Overview

This folder contains a complete UKEF (UK Export Finance) policy analysis agent with comprehensive policy knowledge base and system instructions.

**Files included:**
- `run_agent.py` - Main agent script (Python/Agent Framework)
- `requirements.txt` - Dependencies
- `ukef_policy_knowledge.json` - UKEF policy rules and decision framework (JSON)
- `SYSTEM_INSTRUCTIONS.md` - Agent system prompt and guidelines
- `FIX_SUMMARY.md` - Technical documentation of API migration

## 🎯 What This Agent Does

The agent analyzes export financing eligibility for UK companies seeking UKEF support by:

1. **Checking the 5% Rule**: Verifies export revenue ≥5% in EACH of last 3 financial years
2. **Assessing Export Intensity**: Checks if company qualifies for premium support (20% threshold)
3. **Evaluating Country Risk**: Analyzes destination country's political/economic stability
4. **Verifying Requirements**: Checks UK content (≥20%) and contract value (≥£5m)

## 💾 Data Currently Fed to Agent

**Company Profile:** Kamil Changan Consultancy
```
- Location: UK-based
- Export History (3 years):
  * Year 1 (2023-2024): 5% of annual turnover
  * Year 2 (2024-2025): 5% of annual turnover
  * Year 3 (2025-2026): 7% of annual turnover
- Status: ✅ MEETS 5% Rule (lowest GEF threshold)
- Project: Consultancy in South Sudan
- Country Risk: 🚫 HIGH (requires Principal-level review)
```

**Assessment Result:**
- ✅ Eligible for General Export Facility (GEF)
- ⚠️ NOT eligible for Export Development Guarantee (needs 20%)
- 📋 CONDITIONAL: Requires case-by-case Principal review due to South Sudan risk

## 🚀 How to Use in Azure AI Foundry

### Option 1: Upload Knowledge Base (Recommended)

1. **Open Azure AI Foundry** → Your Agent
2. **Go to "Knowledge Base"** or **"Files"** section
3. **Upload** `ukef_policy_knowledge.json`
   - This file contains all UKEF policies in structured JSON format
   - Agent can reference it for policy lookups
4. **Go to System Instructions**
5. **Copy content from** `SYSTEM_INSTRUCTIONS.md`
   - Paste into agent's system prompt
6. **Save and Test**

### Option 2: Via API/SDK

```python
# Install dependencies
pip install -r requirements.txt

# Run the local agent
python run_agent.py
```

## 📊 Knowledge Base Structure

The `ukef_policy_knowledge.json` contains:

```json
{
  "eligibility_rules": {
    "5_percent_rule": {
      "description": "Must show ≥5% export revenue in EACH of last 3 years",
      "example": {...}
    },
    "20_percent_rule": {
      "description": "Premium support: ≥20% export intensity",
      "example": {...}
    }
  },
  "country_risk_assessment": {
    "south_sudan": {
      "political_risk": "HIGH",
      "approval_requirement": "Principal-level review",
      "required_assessments": [...]
    }
  },
  "assessment_framework": {
    "decision_logic": {...},
    "red_flags": [...]
  },
  "academic_references": {
    "[11] Koomey (2011)",
    "[17] Merz (2023)",
    "[24] Rees (2023)",
    "[8] Jang (ICML 2025)"
  }
}
```

## 🔄 How to Customize for Different Cases

### To assess a different company:

Edit `run_agent.py`:
```python
case_data = """
[Your Company Name]
- Location: [Country]
- Export History (last 3 financial years):
  * Year 1: [percentage]%
  * Year 2: [percentage]%
  * Year 3: [percentage]%
- Proposed Project: [Description]
- Project Value: [£ amount]
- UK Content: [percentage]%
"""
```

### To add more policies:

Edit `ukef_policy_knowledge.json` and add to appropriate section:
```json
{
  "eligibility_rules": {
    "new_policy_name": {
      "description": "...",
      "applicability": "...",
      "threshold": "..."
    }
  }
}
```

## 📝 Key Policies Encoded

### The 5% Rule (GEF Basic Eligibility)
- **Requirement**: ≥5% export revenue in EACH of last 3 years
- **Status**: MUST be met for all years (not average)
- **Application**: General Export Facility (GEF)

### The 20% Rule (Premium Support)
- **Requirement**: ≥20% export intensity (last year OR 3-year average)
- **Application**: Export Development Guarantee, premium facilities

### UK Content Requirement
- **Requirement**: ≥20% of contract value from UK sources
- **Application**: All facilities

### Country Risk Framework
- **South Sudan**: Off-Cover/Restricted status
- **Requirements**: Principal-level review + OECD sustainability check + self-funding verification

## 🔗 How to Upload to Azure AI Foundry

### Step-by-Step:

1. **Navigate to Azure AI Foundry**
   - URL: https://ai.azure.com

2. **Open Your Agent Project**
   - Select your UKEF agent

3. **Access Knowledge Base**
   - Look for "Knowledge Base", "Files", or "Documents" section

4. **Upload Method A - Direct File Upload**
   ```
   Click "Upload" → Select ukef_policy_knowledge.json
   ```

5. **Upload Method B - Via Text Editor**
   ```
   1. Copy entire content of ukef_policy_knowledge.json
   2. Paste into knowledge base text editor
   3. Label as "UKEF_Policies_Knowledge" or similar
   ```

6. **Update System Instructions**
   ```
   1. Go to Agent Settings → System Prompt/Instructions
   2. Copy content from SYSTEM_INSTRUCTIONS.md
   3. Paste and save
   ```

7. **Test the Agent**
   - Ask: "Should we support Kamil Changan for South Sudan?"
   - Agent should now reference the knowledge base

## 📚 Sample Queries to Test

```
1. "Check Kamil Changan's eligibility under the 5% rule"
   → Should reference 3-year history and confirm eligibility

2. "Analyze South Sudan country risk for this project"
   → Should cite high political risk and need for Principal review

3. "What are UKEF's eligibility criteria?"
   → Should return structured policy rules from knowledge base

4. "Does Kamil Changan meet the 20% export intensity threshold?"
   → Should clarify 5-7% vs 20% requirement distinction
```

## 🛠️ Technical Details

**Agent Framework Used:** Microsoft Agent Framework (v1.0.0b260130)
**Model:** gpt-4o-mini (deployment name)
**Language:** Python 3.11+
**Async:** Yes (asyncio-compatible)

## 📖 References Included

- [11] Koomey (2011) - Operational efficiency metrics
- [17] Merz (2023) - Environmental indicators
- [24] Rees (2023) - Environmental policy compliance
- [8] Jang (ICML 2025) - ML-based risk assessment

## ⚠️ Important Notes

- **Export % must meet threshold in EACH year**, not average
- **South Sudan is Off-Cover** - requires special approval
- **Principal-level review** needed for companies <20% export intensity
- **Documentation** of all assumptions required in final assessment

## 🔐 Configuration Checklist

Before running:
- [ ] Set `AGENT_ID` to your actual agent ID from Azure AI Foundry
- [ ] Verify `ENDPOINT` matches your project
- [ ] Confirm `MODEL_DEPLOYMENT_NAME` is correct
- [ ] Update `case_data` with company information
- [ ] Upload `ukef_policy_knowledge.json` to agent's knowledge base
- [ ] Update agent system instructions with `SYSTEM_INSTRUCTIONS.md`

## 📞 Support

For issues or questions:
1. Check `FIX_SUMMARY.md` for API troubleshooting
2. Verify `SYSTEM_INSTRUCTIONS.md` is properly configured
3. Ensure `ukef_policy_knowledge.json` is properly formatted

---

**Ready to use!** Upload the knowledge base files to Azure AI Foundry and your UKEF agent will have access to comprehensive policy rules for accurate eligibility assessment.
