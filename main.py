from core.registry import registry
from core.engine import ExecutionEngine
from report import save_report

# AccountPolicyRequirement
import stigs.ubtu_22_411035
import stigs.ubtu_22_412025
import stigs.ubtu_22_412020
import stigs.ubtu_22_412015

# IdentityUniquenessRequirement
import stigs.ubtu_22_411015
import stigs.ubtu_22_411020
import stigs.ubtu_22_411025
import stigs.ubtu_22_411030

# RequiredFileRequirement
import stigs.ubtu_22_412010
import stigs.ubtu_22_412000
import stigs.ubtu_22_412005
import stigs.ubtu_22_232155
import stigs.ubtu_22_232160

# FileGroupRequirement
import stigs.ubtu_22_232135
import stigs.ubtu_22_232170
import stigs.ubtu_22_232185

# FileOwnerRequirement
import stigs.ubtu_22_232140
import stigs.ubtu_22_611010
import stigs.ubtu_22_611020

# FilePermissionRequirement
import stigs.ubtu_22_232030
import stigs.ubtu_22_232035
import stigs.ubtu_22_612020
import stigs.ubtu_22_612010

# PackageInstalledRequirement
import stigs.ubtu_22_232150

# TMOUTRequirement
import stigs.ubtu_22_412030


def main():
    engine = ExecutionEngine(registry)
    results = engine.run()
    save_report(results)
    print("\n===== SCAN RESULTS =====\n")
    for result in results:
        print(f"{result.stig_id}" f" -> " f"{result.status}")
    print("\nReport saved successfully.")


if __name__ == "__main__":
    main()
