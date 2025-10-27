# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 10:54:45

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 272
- **总 Thread 数**: 23
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 20 threads (262 邮件)
- **RFC**: 1 threads (1 邮件)
- **Bug Report**: 1 threads (7 邮件)
- **GIT PULL**: 1 threads (2 邮件)

---

## 📌 PATCH

共 20 个 thread

---

### Thread 1: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support

**📧 邮件数**: 72 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 11 Jun 2025 15:45:03 -0700

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（内核虚拟机）和 IOMMU（输入输出内存管理单元）在设备中断处理方面的多个补丁和改进，主要集中在对设备发布中断（posted IRQs）的支持和相关逻辑的重构。

1. **原始补丁/问题内容**：
   本系列补丁旨在全面改进 KVM 对设备发布中断的支持，特别是与 IOMMU 交互的部分。补丁包括修复与 AMD 相关的多个问题，优化 IRQ 路由和更新逻辑，减少不必要的代码冗余。

2. **之前讨论要点**：
   之前的讨论主要集中在如何清理和重构 KVM 中与中断处理相关的代码，确保在不同架构（如 x86 和 arm64）中能够有效地处理设备发布中断。讨论中提到，现有的 IRQ 路由和处理逻辑存在复杂性，导致维护困难。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，参与者提出了多个补丁，包括将 IRQ 路由更新逻辑合并到统一的 x86 代码中，简化了对 IRQ 的处理。
   - 讨论中还提到，KVM 应该在更新 IRTE（中断重映射表项）时，避免不必要的检查，以提高性能。
   - 另外，补丁中增加了对 AVIC（高级虚拟化中断控制器）状态的管理，确保在虚拟 CPU 被阻塞时，能够正确处理中断。
   - 最后，参与者一致同意补丁的方向，并对代码进行了多次审查和确认，确保其在不同硬件平台上的兼容性和稳定性。

总的来说，本周的讨论和补丁提交进一步推动了 KVM 在设备中断处理方面的改进，旨在提升系统的性能和可靠性。

#### 📝 邮件列表

1. **[06-11 15:45]** [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-11 15:45]** [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type
 changes as changes
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-11 15:45]** [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-11 15:45]** [PATCH v3 03/62] KVM: Pass new routing entries and irqfd when
 updating IRTEs
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-11 15:45]** [PATCH v3 04/62] KVM: SVM: Track per-vCPU IRTEs using
 kvm_kernel_irqfd structure
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-11 15:45]** [PATCH v3 05/62] KVM: SVM: Delete IRTE link from previous vCPU before
 setting new IRTE
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-11 15:45]** [PATCH v3 06/62] iommu/amd: KVM: SVM: Delete now-unused
 cached/previous GA tag fields
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-11 15:45]** [PATCH v3 07/62] KVM: SVM: Delete IRTE link from previous vCPU
 irrespective of new routing
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[06-11 15:45]** [PATCH v3 08/62] KVM: SVM: Drop pointless masking of default APIC
 base when setting V_APIC_BAR
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-11 15:45]** [PATCH v3 09/62] KVM: SVM: Drop pointless masking of kernel page pa's
 with AVIC HPA masks
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[06-11 15:45]** [PATCH v3 10/62] KVM: SVM: Add helper to deduplicate code for getting
 AVIC backing page
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[06-11 15:45]** [PATCH v3 11/62] KVM: SVM: Drop vcpu_svm's pointless
 avic_backing_page field
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[06-11 15:45]** [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead of
 rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[06-11 15:45]** [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on ID
 during vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[06-11 15:45]** [PATCH v3 14/62] KVM: SVM: Track AVIC tables as natively sized
 pointers, not "struct pages"
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[06-11 15:45]** [PATCH v3 15/62] KVM: SVM: Drop superfluous "cache" of AVIC Physical
 ID entry pointer
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[06-11 15:45]** [PATCH v3 16/62] KVM: VMX: Move enable_ipiv knob to common x86
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[06-11 15:45]** [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set IsRunning
 if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[06-11 15:45]** [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization if CPU
 has erratum #1235
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[06-11 15:45]** [PATCH v3 19/62] KVM: VMX: Suppress PI notifications whenever the
 vCPU is put
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[06-11 15:45]** [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[06-11 15:45]** [PATCH v3 21/62] iommu/amd: KVM: SVM: Use pi_desc_addr to derive ga_root_ptr
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[06-11 15:45]** [PATCH v3 22/62] iommu/amd: KVM: SVM: Pass NULL @vcpu_info to
 indicate "not guest mode"
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[06-11 15:45]** [PATCH v3 23/62] KVM: SVM: Stop walking list of routing table entries
 when updating IRTE
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[06-11 15:45]** [PATCH v3 24/62] KVM: VMX: Stop walking list of routing table entries
 when updating IRTE
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[06-11 15:45]** [PATCH v3 25/62] KVM: SVM: Extract SVM specific code out of get_pi_vcpu_info()
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[06-11 15:45]** [PATCH v3 26/62] KVM: x86: Move IRQ routing/delivery APIs from x86.c
 => irq.c
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-11 15:45]** [PATCH v3 27/62] KVM: x86: Nullify irqfd->producer after updating IRTEs
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[06-11 15:45]** [PATCH v3 28/62] KVM: x86: Dedup AVIC vs. PI code for identifying
 target vCPU
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[06-11 15:45]** [PATCH v3 29/62] KVM: x86: Move posted interrupt tracepoint to common code
   - 发件人: Sean Christopherson <seanjc@google.com>
31. **[06-11 15:45]** [PATCH v3 30/62] KVM: SVM: Clean up return handling in avic_pi_update_irte()
   - 发件人: Sean Christopherson <seanjc@google.com>
32. **[06-11 15:45]** [PATCH v3 31/62] iommu: KVM: Split "struct vcpu_data" into separate
 AMD vs. Intel structs
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[06-11 15:45]** [PATCH v3 32/62] KVM: Don't WARN if updating IRQ bypass route fails
   - 发件人: Sean Christopherson <seanjc@google.com>
34. **[06-11 15:45]** [PATCH v3 33/62] KVM: Fold kvm_arch_irqfd_route_changed() into kvm_arch_update_irqfd_routing()
   - 发件人: Sean Christopherson <seanjc@google.com>
35. **[06-11 15:45]** [PATCH v3 34/62] KVM: x86: Track irq_bypass_vcpu in common x86 code
   - 发件人: Sean Christopherson <seanjc@google.com>
36. **[06-11 15:45]** [PATCH v3 35/62] KVM: x86: Skip IOMMU IRTE updates if there's no old
 or new vCPU being targeted
   - 发件人: Sean Christopherson <seanjc@google.com>
37. **[06-11 15:45]** [PATCH v3 36/62] KVM: x86: Don't update IRTE entries when old and new
 routes were !MSI
   - 发件人: Sean Christopherson <seanjc@google.com>
38. **[06-11 15:45]** [PATCH v3 37/62] KVM: SVM: Revert IRTE to legacy mode if IOMMU
 doesn't provide IR metadata
   - 发件人: Sean Christopherson <seanjc@google.com>
39. **[06-11 15:45]** [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across IRTE
 updates in IOMMU
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[06-11 15:45]** [PATCH v3 39/62] iommu/amd: Document which IRTE fields
 amd_iommu_update_ga() can modify
   - 发件人: Sean Christopherson <seanjc@google.com>
41. **[06-11 15:45]** [PATCH v3 40/62] iommu/amd: KVM: SVM: Infer IsRun from validity of
 pCPU destination
   - 发件人: Sean Christopherson <seanjc@google.com>
42. **[06-11 15:45]** [PATCH v3 41/62] iommu/amd: Factor out helper for manipulating IRTE
 GA/CPU info
   - 发件人: Sean Christopherson <seanjc@google.com>
43. **[06-11 15:45]** [PATCH v3 42/62] iommu/amd: KVM: SVM: Set pCPU info in IRTE when
 setting vCPU affinity
   - 发件人: Sean Christopherson <seanjc@google.com>
44. **[06-11 15:45]** [PATCH v3 43/62] iommu/amd: KVM: SVM: Add IRTE metadata to affined
 vCPU's list if AVIC is inhibited
   - 发件人: Sean Christopherson <seanjc@google.com>
45. **[06-11 15:45]** [PATCH v3 44/62] KVM: SVM: Don't check for assigned device(s) when
 updating affinity
   - 发件人: Sean Christopherson <seanjc@google.com>
46. **[06-11 15:45]** [PATCH v3 45/62] KVM: SVM: Don't check for assigned device(s) when
 activating AVIC
   - 发件人: Sean Christopherson <seanjc@google.com>
47. **[06-11 15:45]** [PATCH v3 46/62] KVM: SVM: WARN if (de)activating guest mode in IOMMU fails
   - 发件人: Sean Christopherson <seanjc@google.com>
48. **[06-11 15:45]** [PATCH v3 47/62] KVM: SVM: Process all IRTEs on affinity change even
 if one update fails
   - 发件人: Sean Christopherson <seanjc@google.com>
49. **[06-11 15:45]** [PATCH v3 48/62] KVM: SVM: WARN if updating IRTE GA fields in IOMMU fails
   - 发件人: Sean Christopherson <seanjc@google.com>
50. **[06-11 15:45]** [PATCH v3 49/62] KVM: x86: Drop superfluous "has assigned device"
 check in kvm_pi_update_irte()
   - 发件人: Sean Christopherson <seanjc@google.com>
51. **[06-11 15:45]** [PATCH v3 50/62] KVM: x86: WARN if IRQ bypass isn't supported in kvm_pi_update_irte()
   - 发件人: Sean Christopherson <seanjc@google.com>
52. **[06-11 15:45]** [PATCH v3 51/62] KVM: x86: WARN if IRQ bypass routing is updated
 without in-kernel local APIC
   - 发件人: Sean Christopherson <seanjc@google.com>
53. **[06-11 15:45]** [PATCH v3 52/62] KVM: SVM: WARN if ir_list is non-empty at vCPU free
   - 发件人: Sean Christopherson <seanjc@google.com>
54. **[06-11 15:45]** [PATCH v3 53/62] KVM: x86: Decouple device assignment from IRQ bypass
   - 发件人: Sean Christopherson <seanjc@google.com>
55. **[06-11 15:45]** [PATCH v3 54/62] KVM: VMX: WARN if VT-d Posted IRQs aren't possible
 when starting IRQ bypass
   - 发件人: Sean Christopherson <seanjc@google.com>
56. **[06-11 15:45]** [PATCH v3 55/62] KVM: SVM: Use vcpu_idx, not vcpu_id, for GA log tag/metadata
   - 发件人: Sean Christopherson <seanjc@google.com>
57. **[06-11 15:45]** [PATCH v3 56/62] iommu/amd: WARN if KVM calls GA IRTE helpers without
 virtual APIC support
   - 发件人: Sean Christopherson <seanjc@google.com>
58. **[06-11 15:46]** [PATCH v3 57/62] KVM: SVM: Fold avic_set_pi_irte_mode() into its sole caller
   - 发件人: Sean Christopherson <seanjc@google.com>
59. **[06-11 15:46]** [PATCH v3 58/62] KVM: SVM: Don't check vCPU's blocking status when
 toggling AVIC on/off
   - 发件人: Sean Christopherson <seanjc@google.com>
60. **[06-11 15:46]** [PATCH v3 59/62] KVM: SVM: Consolidate IRTE update when toggling AVIC on/off
   - 发件人: Sean Christopherson <seanjc@google.com>
61. **[06-11 15:46]** [PATCH v3 60/62] iommu/amd: KVM: SVM: Allow KVM to control need for
 GA log interrupts
   - 发件人: Sean Christopherson <seanjc@google.com>
62. **[06-11 15:46]** [PATCH v3 61/62] KVM: SVM: Generate GA log IRQs only if the
 associated vCPUs is blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
63. **[06-11 15:46]** [PATCH v3 62/62] KVM: x86: Rename kvm_set_msi_irq() => kvm_msi_to_lapic_irq()
   - 发件人: Sean Christopherson <seanjc@google.com>
64. **[06-12 12:59]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Marc Zyngier <maz@kernel.org>
65. **[06-12 07:34]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
66. **[06-13 19:45]** Re: [PATCH v3 08/62] KVM: SVM: Drop pointless masking of default
 APIC base when setting V_APIC_BAR
   - 发件人: Naveen N Rao <naveen@kernel.org>
67. **[06-13 20:07]** Re: [PATCH v3 09/62] KVM: SVM: Drop pointless masking of kernel page
 pa's with AVIC HPA masks
   - 发件人: Naveen N Rao <naveen@kernel.org>
68. **[06-13 20:08]** Re: [PATCH v3 10/62] KVM: SVM: Add helper to deduplicate code for
 getting AVIC backing page
   - 发件人: Naveen N Rao <naveen@kernel.org>
69. **[06-13 20:14]** Re: [PATCH v3 11/62] KVM: SVM: Drop vcpu_svm's pointless
 avic_backing_page field
   - 发件人: Naveen N Rao <naveen@kernel.org>
70. **[06-13 12:43]** Re: [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type
 changes as changes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
71. **[06-13 13:47]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
72. **[06-13 13:50]** Re: [PATCH v3 33/62] KVM: Fold kvm_arch_irqfd_route_changed() into
 kvm_arch_update_irqfd_routing()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 2: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 46 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 11 Jun 2025 11:47:57 +0100

#### 🤖 AI 总结

本邮件列表讨论的主题是关于在 KVM 中支持 Arm CCA（Confidential Compute Architecture）的补丁系列（PATCH v9 00/43）。该补丁旨在实现受保护虚拟机的运行，主要涉及以下几个方面：

1. **原始补丁内容**：该补丁系列为 KVM 添加了对 Arm CCA 的支持，允许在 KVM 中运行受保护的虚拟机。相关的客人支持已在 v6.14-rc1 中合并。

2. **历史讨论要点**：之前的讨论集中在如何处理 KVM 中的内存管理、虚拟 CPU 状态、以及如何与 RMM（Realm Management Monitor）进行交互。补丁中涉及的主要改动包括对 RTT（Realm Translation Table）的管理、对内存访问的处理、以及如何在进入和退出 Realm 时进行状态管理。

3. **本周的新讨论和进展**：本周的讨论中，补丁的多个方面得到了更新和修正，包括：
   - 增加了对 Realm 中的 MMIO（内存映射输入输出）仿真支持。
   - 允许用户空间通过 KVM_SET_ONE_REG 设置断点和观察点。
   - 增加了对 Realm 中的定时器支持。
   - 处理了 Realm 中的 RIPAS（Realm IPA State）变化请求。
   - 讨论了如何在 Realm 中管理 PMU（性能监控单元）中断。

此外，邮件中还提到了一些代码的清理和重构，确保补丁的可维护性和性能。整体来看，这一系列补丁的目标是增强 KVM 对 Arm CCA 的支持，确保在受保护环境中能够有效地管理虚拟机的资源和状态。

#### 📝 邮件列表

1. **[06-11 11:47]** [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[06-11 11:47]** [PATCH v9 01/43] kvm: arm64: Include kvm_emulate.h in kvm/arm_psci.h
   - 发件人: Steven Price <steven.price@arm.com>
3. **[06-11 11:47]** [PATCH v9 02/43] arm64: RME: Handle Granule Protection Faults (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
4. **[06-11 11:48]** [PATCH v9 03/43] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
5. **[06-11 11:48]** [PATCH v9 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
6. **[06-11 11:48]** [PATCH v9 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
7. **[06-11 11:48]** [PATCH v9 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
8. **[06-11 11:48]** [PATCH v9 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
9. **[06-11 11:48]** [PATCH v9 08/43] kvm: arm64: Don't expose debug capabilities for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
10. **[06-11 11:48]** [PATCH v9 09/43] KVM: arm64: Allow passing machine type in KVM creation
   - 发件人: Steven Price <steven.price@arm.com>
11. **[06-11 11:48]** [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
12. **[06-11 11:48]** [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
13. **[06-11 11:48]** [PATCH v9 12/43] KVM: arm64: vgic: Provide helper for number of list registers
   - 发件人: Steven Price <steven.price@arm.com>
14. **[06-11 11:48]** [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
15. **[06-11 11:48]** [PATCH v9 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
16. **[06-11 11:48]** [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
17. **[06-11 11:48]** [PATCH v9 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
18. **[06-11 11:48]** [PATCH v9 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
19. **[06-11 11:48]** [PATCH v9 18/43] KVM: arm64: Handle realm MMIO emulation
   - 发件人: Steven Price <steven.price@arm.com>
20. **[06-11 11:48]** [PATCH v9 19/43] arm64: RME: Allow populating initial contents
   - 发件人: Steven Price <steven.price@arm.com>
21. **[06-11 11:48]** [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
22. **[06-11 11:48]** [PATCH v9 21/43] KVM: arm64: Handle realm VCPU load
   - 发件人: Steven Price <steven.price@arm.com>
23. **[06-11 11:48]** [PATCH v9 22/43] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
24. **[06-11 11:48]** [PATCH v9 23/43] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Steven Price <steven.price@arm.com>
25. **[06-11 11:48]** [PATCH v9 24/43] KVM: arm64: WARN on injected undef exceptions
   - 发件人: Steven Price <steven.price@arm.com>
26. **[06-11 11:48]** [PATCH v9 25/43] arm64: Don't expose stolen time for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
27. **[06-11 11:48]** [PATCH v9 26/43] arm64: RME: allow userspace to inject aborts
   - 发件人: Steven Price <steven.price@arm.com>
28. **[06-11 11:48]** [PATCH v9 27/43] arm64: RME: support RSI_HOST_CALL
   - 发件人: Steven Price <steven.price@arm.com>
29. **[06-11 11:48]** [PATCH v9 28/43] arm64: RME: Allow checking SVE on VM instance
   - 发件人: Steven Price <steven.price@arm.com>
30. **[06-11 11:48]** [PATCH v9 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Steven Price <steven.price@arm.com>
31. **[06-11 11:48]** [PATCH v9 30/43] arm64: RME: Prevent Device mappings for Realms
   - 发件人: Steven Price <steven.price@arm.com>
32. **[06-11 11:48]** [PATCH v9 31/43] arm_pmu: Provide a mechanism for disabling the physical IRQ
   - 发件人: Steven Price <steven.price@arm.com>
33. **[06-11 11:48]** [PATCH v9 32/43] arm64: RME: Enable PMU support with a realm guest
   - 发件人: Steven Price <steven.price@arm.com>
34. **[06-11 11:48]** [PATCH v9 33/43] arm64: RME: Hide KVM_CAP_READONLY_MEM for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
35. **[06-11 11:48]** [PATCH v9 34/43] arm64: RME: Propagate number of breakpoints and watchpoints to userspace
   - 发件人: Steven Price <steven.price@arm.com>
36. **[06-11 11:48]** [PATCH v9 35/43] arm64: RME: Set breakpoint parameters through SET_ONE_REG
   - 发件人: Steven Price <steven.price@arm.com>
37. **[06-11 11:48]** [PATCH v9 36/43] arm64: RME: Initialize PMCR.N with number counter supported by RMM
   - 发件人: Steven Price <steven.price@arm.com>
38. **[06-11 11:48]** [PATCH v9 37/43] arm64: RME: Propagate max SVE vector length from RMM
   - 发件人: Steven Price <steven.price@arm.com>
39. **[06-11 11:48]** [PATCH v9 38/43] arm64: RME: Configure max SVE vector length for a Realm
   - 发件人: Steven Price <steven.price@arm.com>
40. **[06-11 11:48]** [PATCH v9 39/43] arm64: RME: Provide register list for unfinalized RME RECs
   - 发件人: Steven Price <steven.price@arm.com>
41. **[06-11 11:48]** [PATCH v9 40/43] arm64: RME: Provide accurate register list
   - 发件人: Steven Price <steven.price@arm.com>
42. **[06-11 11:48]** [PATCH v9 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>
43. **[06-11 11:48]** [PATCH v9 42/43] KVM: arm64: Expose KVM_ARM_VCPU_REC to user space
   - 发件人: Steven Price <steven.price@arm.com>
44. **[06-11 11:48]** [PATCH v9 43/43] KVM: arm64: Allow activating realms
   - 发件人: Steven Price <steven.price@arm.com>
45. **[06-12 16:14]** Re: [PATCH v9 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Joey Gouly <joey.gouly@arm.com>
46. **[06-12 16:32]** Re: [PATCH v9 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 3: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 30 | **👥 参与者**: 6 | **📅 开始时间**: Wed, 11 Jun 2025 14:33:12 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 的补丁系列，主要目的是在主机上映射由 `guest_memfd` 支持的内存，以增强软件保护虚拟机的安全性。

1. **原始补丁内容**：该补丁系列（PATCH v12 00/18）旨在支持在主机上映射 `guest_memfd` 支持的内存。此功能对像 Firecracker 这样的虚拟机管理程序非常有用，能够增强对类似 Spectre 的攻击的防护。

2. **历史讨论要点**：之前的讨论主要集中在补丁的反馈和重构上，包括对 `CONFIG_KVM_PRIVATE_MEM` 和相关函数的重命名，以更清晰地反映其目的。此外，补丁还引入了对共享内存的支持，并为此设置了新的配置选项。

3. **本周的新讨论与进展**：本周的讨论中，参与者对补丁进行了审查和反馈，确认了多个补丁的有效性。特别是补丁 8（允许主机映射 `guest_memfd` 页面）和补丁 18（扩展自测以测试映射功能）得到了积极的评价。讨论中还提到了一些术语的混淆问题，建议在命名时使用更明确的术语。此外，针对特定虚拟机类型的共享内存支持也进行了详细讨论，确保补丁的适用性和功能性。

总体而言，此次讨论推动了 KVM 在内存管理和安全性方面的进展，并为未来的补丁提供了重要的反馈和建议。

#### 📝 邮件列表

1. **[06-11 14:33]** [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-11 14:33]** [PATCH v12 01/18] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-11 14:33]** [PATCH v12 02/18] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-11 14:33]** [PATCH v12 03/18] KVM: Rename kvm_arch_has_private_mem() to kvm_arch_supports_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[06-11 14:33]** [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[06-11 14:33]** [PATCH v12 05/18] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[06-11 14:33]** [PATCH v12 06/18] KVM: Fix comments that refer to slots_lock
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[06-11 14:33]** [PATCH v12 07/18] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[06-11 14:33]** [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[06-11 14:33]** [PATCH v12 09/18] KVM: guest_memfd: Track shared memory support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[06-11 14:33]** [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[06-11 14:33]** [PATCH v12 11/18] KVM: x86: Consult guest_memfd when computing max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[06-11 14:33]** [PATCH v12 12/18] KVM: x86: Enable guest_memfd shared memory for
 non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[06-11 14:33]** [PATCH v12 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[06-11 14:33]** [PATCH v12 14/18] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[06-11 14:33]** [PATCH v12 15/18] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[06-11 14:33]** [PATCH v12 16/18] KVM: Introduce the KVM capability KVM_CAP_GMEM_SHARED_MEM
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[06-11 14:33]** [PATCH v12 17/18] KVM: selftests: Don't use hardcoded page sizes in
 guest_memfd test
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[06-11 14:33]** [PATCH v12 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[06-12 21:46]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Shivank Garg <shivankg@amd.com>
21. **[06-12 21:53]** Re: [PATCH v12 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Shivank Garg <shivankg@amd.com>
22. **[06-12 21:54]** Re: [PATCH v12 17/18] KVM: selftests: Don't use hardcoded page sizes
 in guest_memfd test
   - 发件人: Shivank Garg <shivankg@amd.com>
23. **[06-12 10:33]** Re: [PATCH v12 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: James Houghton <jthoughton@google.com>
24. **[06-12 19:38]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
25. **[06-13 06:57]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Ackerley Tng <ackerleytng@google.com>
26. **[06-13 13:35]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[06-13 14:03]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-13 23:18]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
29. **[06-13 15:08]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[06-13 15:48]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 4: [PATCH v11 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 18 | **👥 参与者**: 5 | **📅 开始时间**: Thu,  5 Jun 2025 16:37:42 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）的补丁系列，主要涉及在主机上映射基于 guest_memfd 的内存，以支持软件保护的虚拟机。

1. **原始补丁内容**：补丁系列的核心是允许主机映射 guest_memfd 支持的共享内存，这一功能通过 KVM_GMEM_SHARED_MEM Kconfig 选项进行控制，并在创建时通过 GUEST_MEMFD_FLAG_SUPPORT_SHARED 标志启用。补丁还包括对 KVM/arm64 的用户内存错误处理进行重构，以及对嵌套虚拟化的支持。

2. **之前讨论要点**：在历史讨论中，开发者 Fuad Tabba 对补丁进行了多次修改，增加了边界检查和自测，重构了错误处理代码，并解决了之前版本中的反馈意见。参与者们对补丁的不同部分进行了审查和确认（如 Acked 和 Reviewed-by 标签）。

3. **本周的新讨论和进展**：本周的讨论主要集中在对补丁的细节审查上。Gavin Shan 对多个补丁提出了建议和修改意见，包括对内存缓存初始化的讨论以及对错误返回值的处理。其他参与者也对补丁提出了优化建议，强调代码的清晰性和安全性。整体来看，补丁得到了积极的反馈，预计将在后续版本中进行进一步修改和完善。

#### 📝 邮件列表

1. **[06-05 16:37]** [PATCH v11 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-05 16:37]** [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-05 16:37]** [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-05 16:37]** [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[06-05 16:37]** [PATCH v11 15/18] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[06-05 16:38]** [PATCH v11 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[06-06 11:12]** Re: [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
8. **[06-09 09:43]** Re: [PATCH v11 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[06-09 10:27]** Re: [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Gavin Shan <gshan@redhat.com>
10. **[06-09 10:29]** Re: [PATCH v11 15/18] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Gavin Shan <gshan@redhat.com>
11. **[06-09 14:08]** Re: [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Gavin Shan <gshan@redhat.com>
12. **[06-09 08:01]** Re: [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[06-09 08:04]** Re: [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[06-09 08:06]** Re: [PATCH v11 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[06-09 19:02]** Re: [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Gavin Shan <gshan@redhat.com>
16. **[06-09 19:06]** Re: [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Gavin Shan <gshan@redhat.com>
17. **[06-11 11:59]** Re: [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Shivank Garg <shivankg@amd.com>
18. **[06-11 11:20]** Re: [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 5: [PATCH v7 00/14] arm: rework id register storage

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 06 Jun 2025 11:53:15 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM 架构的 ID 寄存器存储重构的补丁（PATCH v7 00/14）。该补丁旨在重新组织和存储 ARM CPU 的 ID 寄存器，以提高代码的可维护性和可读性。

在历史讨论中，Cornelia Huck 提出了对补丁的友好提醒，询问是否还有其他需要处理的事项。之前的讨论主要集中在补丁的编译问题上，Peter Maydell 指出多个补丁在编译时出现错误，尤其是类型不兼容的问题。

本周的新讨论中，Peter Maydell 和 Cornelia Huck 继续探讨补丁的具体实现细节。Peter 指出在某些补丁中，编译错误并未在他的环境中出现，可能是由于配置或编译器版本的不同。Cornelia 提出了对生成脚本的建议，认为应使用 Python 而非 awk，并要求生成的源文件添加注释以说明其自动生成的性质。此外，讨论中还提到了一些寄存器的包含问题，认为某些寄存器并不适合被纳入 ID 寄存器的定义中。

总体来看，本周的讨论主要围绕补丁的编译问题、生成脚本的改进建议以及寄存器定义的合理性展开，参与者们积极交流以推动补丁的完善。

#### 📝 邮件列表

1. **[06-06 11:53]** Re: [PATCH v7 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[06-12 16:04]** Re: [PATCH v7 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
3. **[06-12 16:16]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
4. **[06-12 16:29]** Re: [PATCH v7 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
5. **[06-12 17:34]** Re: [PATCH v7 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[06-12 16:35]** Re: [PATCH v7 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
7. **[06-12 17:36]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[06-12 16:36]** Re: [PATCH v7 00/14] arm: rework id register storage
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
9. **[06-12 16:39]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
10. **[06-12 16:39]** Re: [PATCH v7 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
11. **[06-12 17:42]** Re: [PATCH v7 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[06-12 17:53]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[06-12 18:07]** Re: [PATCH v7 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 6: [PATCH 0/8] KVM: Remove include/kvm, standardize includes

**📧 邮件数**: 12 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 10 Jun 2025 17:10:34 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主题为“移除 include/kvm，标准化包含路径”。该补丁系列包含八个补丁，旨在通过文件移动和重命名，清理 KVM 的包含路径，并在所有架构中实现标准化。

在历史讨论中，补丁的背景是为了支持 Colton 的分区 PMU 系列工作，同时也为 KVM 的多实例支持做准备。虽然多实例的想法已被放弃，但开发者希望逐步上游一些有益的代码。

本周的新讨论中，Sean Christopherson 提出了多个补丁，主要内容包括：
1. 将 ARM 特定的头文件移至架构目录，减少对其他架构的暴露。
2. 将最后一个保留在 include/kvm 的文件 iodev.h 移至标准的 include/linux 目录，并删除 include/kvm。
3. 停止在 MIPS、PPC 和 s390 的构建路径中添加 virt/kvm，以确保这些头文件仅供核心 KVM 代码使用。
4. 标准化所有架构的 KVM 包含路径，确保一致性。

讨论中还提到，Paolo Bonzini 表示希望尽快将这些补丁提交到 kvm/next，且得到了其他开发者的认可和支持。整体来看，这一系列补丁将有助于简化 KVM 的代码结构，提升可维护性。

#### 📝 邮件列表

1. **[06-10 17:10]** [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-10 17:10]** [PATCH 1/8] KVM: arm64: Move arm_{psci,hypercalls}.h to an internal
 KVM path
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-10 17:10]** [PATCH 2/8] KVM: arm64: Include KVM headers to get forward declarations
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-10 17:10]** [PATCH 3/8] KVM: arm64: Move ARM specific headers in include/kvm to
 arch directory
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-10 17:10]** [PATCH 4/8] KVM: Move include/kvm/iodev.h to include/linux as kvm_iodev.h
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-10 17:10]** [PATCH 5/8] KVM: MIPS: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-10 17:10]** [PATCH 6/8] KVM: PPC: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-10 17:10]** [PATCH 7/8] KVM: s390: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[06-10 17:10]** [PATCH 8/8] KVM: Standardize include paths across all architectures
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-12 06:56]** Re: [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
11. **[06-12 15:01]** Re: [PATCH 7/8] KVM: s390: Stop adding virt/kvm to the arch include
 path
   - 发件人: Janosch Frank <frankja@linux.ibm.com>
12. **[06-13 14:02]** Re: [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases fixes

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Thu,  5 Jun 2025 12:36:09 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试修复，主要集中在 arch_timer_edge_cases 的问题上。

1. **原始 patch/问题的内容**：
   Sebastian Ott 提出的补丁（[PATCH v3 0/4]）包含了针对 arch_timer_edge_cases 的小修复，这些问题是在调试 ampere-one 机器上的自测试失败时发现的。补丁的更新包括根据 Marc 的建议确定有效的计数器宽度，并增加了修复 xval 初始化的新补丁。经过多次测试，未发现问题。

2. **之前的讨论要点**：
   在历史讨论中，Sebastian 提到他在多台机器上进行了测试，并未遇到问题。邮件中没有其他参与者的具体反馈。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Miguel Luis 提供了他在不同情况下（包括 HAS_EL2 和 !HAS_EL2_E2H0）对补丁的测试结果，发现某些情况下测试未能返回。Sebastian 表示将尝试重现该问题。Raghavendra Rao Ananta 提出了与 GIC（通用中断控制器）相关的补丁，增加了控制 GICD_TYPER2.nASSGIcap 的属性，并进行了相应的自测试。这些补丁旨在允许用户空间在 VM 级别控制硬件中断注入的支持。最后，Oliver Upton 提出了对补丁的格式化建议，强调了在提交前应运行 checkpatch 工具。

整体来看，本周的讨论主要围绕补丁的测试结果和进一步的功能扩展，参与者积极反馈并提出改进建议。

#### 📝 邮件列表

1. **[06-05 12:36]** [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases fixes
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[06-09 17:26]** Re: [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases fixes
   - 发件人: Miguel Luis <miguel.luis@oracle.com>
3. **[06-10 15:50]** Re: [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases
 fixes
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[06-13 15:52]** [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
5. **[06-13 15:52]** [PATCH v3 1/4] KVM: arm64: Disambiguate support for vSGIs v. vLPIs
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
6. **[06-13 15:52]** [PATCH v3 2/4] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ handling
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
7. **[06-13 15:52]** [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
8. **[06-13 15:52]** [PATCH v3 4/4] KVM: arm64: selftests: Add test for nASSGIcap attribute
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
9. **[06-13 13:53]** Re: [PATCH v3 0/4] KVM: arm64: Add attribute to control
 GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-13 14:25]** Re: [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>

---

### Thread 8: [PATCH v23 0/4] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 11 Jun 2025 13:01:10 -0500

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的分支记录缓冲扩展（BRBE）的支持，主要涉及一系列补丁的提交和讨论。

1. **原始补丁内容**：补丁系列的目标是启用 ARM64 的 BRBE 功能，允许在性能监控中记录分支信息。BRBE 是 ARMv9.2 架构的一项新特性，类似于 x86 的最后分支记录（LBR）功能。

2. **之前讨论要点**：在之前的讨论中，补丁经历了多次重构，修复了与多种系统架构兼容性相关的问题。讨论集中在如何处理 BRBE 的初始化、事件记录和与 KVM 的兼容性等方面。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的测试结果上。参与者 Adam Young 报告了在支持 BRBE 的机器上成功运行测试，使用 `perf` 工具生成的 `perf.data` 文件能够正常处理。此外，补丁的测试结果显示，BRBE 功能在性能监控中表现良好，能够生成有效的输出。Rob Herring 也确认了测试的有效性，并分享了测试方法。

总体来看，本周的讨论确认了 BRBE 的功能实现和测试结果，为后续的合并和应用奠定了基础。

#### 📝 邮件列表

1. **[06-11 13:01]** [PATCH v23 0/4] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[06-11 13:01]** [PATCH v23 1/4] arm64/sysreg: Add BRBE registers and fields
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
3. **[06-11 13:01]** [PATCH v23 2/4] arm64: Handle BRBE booting requirements
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
4. **[06-11 13:01]** [PATCH v23 3/4] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
5. **[06-11 13:01]** [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch Record
 Buffer Extension (BRBE)
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
6. **[06-12 13:13]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Adam Young <admiyo@amperemail.onmicrosoft.com>
7. **[06-12 15:28]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
8. **[06-12 23:16]** Re: [PATCH v23 2/4] arm64: Handle BRBE booting requirements
   - 发件人: Adam Young <admiyo@amperemail.onmicrosoft.com>
9. **[06-12 23:19]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Adam Young <admiyo@amperemail.onmicrosoft.com>

---

### Thread 9: [PATCH v4 0/5] Add FIELD_MODIFY() helper

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 12 Jun 2025 21:46:07 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于添加 `FIELD_MODIFY()` 辅助宏的补丁（PATCH v4 0/5）。该宏旨在替代现有的位域操作方式，提供编译时类型检查，以捕捉参数类型错误。补丁系列还包括将内核核心文件中四个使用 `FIELD_MODIFY()` 的实例转换为新的宏形式，利用 Coccinelle 工具实现。

在历史讨论中，参与者对该补丁的必要性和实现方式进行了探讨。Luo Jie 提到，`FIELD_MODIFY()` 的引入是为了提高代码的安全性和可读性。然而，Marc Zyngier 表达了不同意见，认为现有的辅助函数已经足够，并不需要重复实现相同功能。

本周的新讨论中，Luo Jie 提交了多个补丁，具体包括将 ARM64 架构下的多个文件中的位域操作替换为 `FIELD_MODIFY()`。同时，Marc Zyngier 和 Markus Elfring 对补丁的描述和实现细节提出了改进建议，质疑补丁的必要性，并建议简化代码和文档。

总体来看，尽管补丁的实现已逐步推进，但仍然存在对其必要性和实现方式的争议。

#### 📝 邮件列表

1. **[06-12 21:46]** [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-12 21:46]** [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
3. **[06-12 21:46]** [PATCH v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
4. **[06-12 21:46]** [PATCH v4 3/5] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
5. **[06-12 21:46]** [PATCH v4 4/5] arm64: kvm: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
6. **[06-12 21:46]** [PATCH v4 5/5] arm64: mm: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
7. **[06-12 15:11]** Re: [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[06-12 18:48]** Re: [cocci] [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
9. **[06-12 22:15]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Markus Elfring <Markus.Elfring@web.de>

---

### Thread 10: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 26 May 2025 21:26:52 -0300

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下引入新的内存槽标志，以指示可缓存映射的补丁（PATCH v6 3/5）。该补丁旨在提供一种机制，使虚拟机监控器（VMM）能够通过标志传达其意图。

在历史讨论中，参与者对该补丁的必要性和实现方式进行了激烈辩论。Jason Gunthorpe 表示反对，认为 VFIO（虚拟功能 I/O）无法有效利用该标志，并且内核不允许将可缓存的虚拟内存区域（VMA）切换为不可缓存。Ankit Agrawal 则提到 Oliver 之前支持使用内存槽标志，但未能得到一致认可。Sean Christopherson 进一步指出，该补丁在 KVM 的用户 API 中并不合适，且可能导致混乱。

在本周的新讨论中，Jason Gunthorpe 和 Sean Christopherson 继续探讨了 KVM 如何处理 PFN（页面框架号）映射及其与缓存的关系。Oliver Upton 表示，虽然内存槽标志的想法是为了与 KVM 进行“握手”，但在缺乏完整解决方案的情况下，可以暂时放弃该标志。他强调，VMM 需要根据内存属性来决定如何处理内存槽。

总体来看，尽管补丁的提出引发了多方讨论，但目前尚未达成一致意见，且对实现的必要性和有效性仍存在疑虑。

#### 📝 邮件列表

1. **[05-26 21:26]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
2. **[05-27 04:33]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable
 mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
3. **[06-06 10:57]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-06 11:11]** Re: [PATCH v6 1/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-09 09:24]** Re: [PATCH v6 1/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
6. **[06-09 07:21]** Re: [PATCH v6 1/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-13 12:38]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 11: [PATCH V4 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 12 Jun 2025 09:05:45 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 架构的补丁系列，主要目的是去除冗余的 DBG_MDSCR_* 宏定义。补丁的核心内容是由于 MDSCR_EL1 已在工具的 sysreg 格式中定义，因此可以在所有调试监视器相关的调用路径中使用，从而使得 DBG_MDSCR_* 宏变得多余，建议完全删除。同时，补丁还将处理 MDSCR_EL1 寄存器的变量类型更改为 u64，以反映其真实宽度。

在之前的讨论中，补丁经历了多个版本的修改，主要集中在更新提交信息、分离自测更改以及调整变量类型等方面。参与者们对补丁的合理性表示认可，并提出了一些小的改进建议。

本周的新讨论中，Anshuman Khandual 提出了补丁的最新版本，并回应了其他开发者的建议，计划在补丁中合并对 __cpu_setup 中常量的更改。此外，Marc Zyngier 提出了关于使用 `mov` 指令而非 `mov_q` 的建议，以更好地处理常量。整体来看，讨论氛围积极，补丁的推进顺利，预计将很快合并。

#### 📝 邮件列表

1. **[06-12 09:05]** [PATCH V4 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[06-12 09:05]** [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[06-12 09:05]** [PATCH V4 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[06-12 09:17]** Re: [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[06-12 15:54]** Re: [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[06-12 11:51]** Re: [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH v3 00/10] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 05 Jun 2025 11:48:58 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于支持 Armv8.8 SPE 特性的补丁（PATCH v3 00/10）的内容，主要涉及三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 FEAT_SPE_FDS 数据源过滤。这些特性相互独立，可以单独应用。

在历史讨论中，James Clark 提出了补丁的初步版本，详细说明了每个特性的实现以及所需的系统寄存器变更。补丁中包括了对新寄存器字段的添加和对现有过滤器的支持，经过 Leo Yan 的测试和审核。

在本周的新讨论中，Anshuman Khandual 对补丁进行了进一步的审查。他确认了第一个补丁（关于新寄存器字段的添加）符合 ARM 规范，并对第二个补丁（支持 FEAT_SPEv1p4 过滤器）提出了疑问，询问为何不能直接添加所有新过滤器位，而不使用排除和包含的中介方式。James Clark 回应了这一点，解释了这样做的原因是为了避免重复定义，并保持一致性，认为当前的实现方式更为清晰。

总体来看，本周讨论主要集中在对补丁细节的审查和优化建议上，未发现重大问题。

#### 📝 邮件列表

1. **[06-05 11:48]** [PATCH v3 00/10] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[06-05 11:48]** [PATCH v3 01/10] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: James Clark <james.clark@linaro.org>
3. **[06-05 11:49]** [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[06-12 12:14]** Re: [PATCH v3 01/10] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[06-12 13:05]** Re: [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[06-12 09:42]** Re: [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 13: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 10 Jun 2025 11:01:28 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测中的一个补丁，补丁内容为将 MDSCR_EL1 寄存器的局部变量类型更改为 uint64_t，以反映其真实的寄存器宽度。补丁由 Anshuman Khandual 提交，并得到了 Ada Couprie Diaz 的审核。

在之前的讨论中，Marc Zyngier 对补丁提出了质疑，认为在不重要的地方进行这样的更改并不合适。他指出，arch/arm64/kernel/debug-monitors.c 文件中存在大量对该寄存器的 32 位操作，因此如果要进行更改，应该在所有相关文件中统一处理，而不是随机选择某个文件进行修改。

本周的新讨论中，Anshuman Khandual 对 Marc 的意见进行了回应，提到该补丁系列的第一部分实际上已经在提到的文件中将 mdscr 寄存器更改为 64 位。Mark Rutland 也指出，Anshuman 在补丁的第一部分或封面信中没有抄送 Marc，这可能导致了上下文缺失的问题。Marc 再次强调了在讨论中提供完整上下文的重要性。

总体来看，本周的讨论集中在补丁的合理性和上下文的沟通上，参与者们对如何更全面地处理寄存器类型的更改进行了深入交流。

#### 📝 邮件列表

1. **[06-10 11:01]** [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[06-10 18:01]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-11 09:15]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding
 variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[06-11 10:59]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding
 variables as uint64_t
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[06-11 13:52]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc

**📧 邮件数**: 4 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 10 Jun 2025 20:41:32 +0530

#### 🤖 AI 总结

本邮件讨论主题为修复 KVM 在 arm64 架构下使用 gcc 编译时的构建失败问题。原始的 patch 由 Aneesh Kumar K.V 提出，主要针对在使用 aarch64-linux-gnu-gcc 版本 13.3.0 时出现的未定义引用错误，具体是 `__kvm_nvhe___lshrti3` 函数缺失。为了解决这个问题，patch 中增加了一个新的 helper 函数，类似于之前的提交（commit 9bfe7553fadb）中实现的 `__lshrti3` 函数。

在之前的讨论中，参与者们并未对该问题进行深入探讨，主要集中在 patch 的具体实现上。

本周的新讨论中，Aneesh 提到该问题与 pKVM tracefs 补丁相关，Marc Zyngier 则询问了触发此问题的具体原因，并希望了解如何避免此类问题的再次发生。Vincent Donnefort 进一步指出，相关的文件是为 pKVM 跟踪支持而引入的，但尚未合并到主干中。这表明当前讨论不仅关注构建失败的修复，还涉及到 pKVM 功能的开发进展。

#### 📝 邮件列表

1. **[06-10 20:41]** [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[06-10 20:47]** Re: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
3. **[06-10 16:31]** Re: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[06-10 16:48]** Re: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 15: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 28 May 2025 10:30:20 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（内核虚拟机）在 arm64 架构上添加对 KVM_MEM_USERFAULT 支持的补丁（patch v2 06/13）。该补丁旨在增强内存管理功能，允许在用户空间处理缺页异常。

在历史讨论中，参与者 Sean Christopherson 和 James Houghton 进行了多次交流，主要集中在补丁的代码实现上。Sean 指出补丁存在一些问题，并提供了具体的代码差异（diff），指出在内存区域提交时，某些标志位（flags）可能未正确处理，导致功能不正常。James 则对这些问题表示困惑，并试图澄清代码逻辑。

在本周的新讨论中，James 对 Sean 的反馈表示歉意，并承认自己混淆了 KVM_MEM_USERFAULT 和 KVM_MEM_LOG_DIRTY_PAGES 的概念。他决定撤回之前提到的代码更改，感谢 Sean 的指正。这表明讨论朝着解决问题的方向发展，参与者之间的沟通也更加顺畅。

#### 📝 邮件列表

1. **[05-28 10:30]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[05-28 20:17]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: James Houghton <jthoughton@google.com>
3. **[05-28 16:25]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-09 16:04]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: James Houghton <jthoughton@google.com>

---

### Thread 16: [PATCH V5 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 13 Jun 2025 08:06:44 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 架构的补丁系列，主要内容是删除冗余的 DBG_MDSCR_* 宏，并将与 MDSCR_EL1 寄存器相关的变量类型更改为 uint64_t，以反映其真实宽度。

1. **原始补丁内容**：补丁系列的目标是移除 DBG_MDSCR_* 宏，因为 MDSCR_EL1 已在工具 sysreg 格式中定义，可以在所有调试监视器相关的调用路径中使用。补丁还将处理 MDSCR_EL1 寄存器的所有变量类型更改为 u64。

2. **之前讨论要点**：在之前的版本中，补丁经历了多次修改，包括更新提交信息、将某些变量类型更改为 uint64_t，以及将自测更改拆分为单独的补丁。参与者 Mark 和 Ada 提出了多项建议，帮助改进补丁的实现。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的 V5 版本上，Anshuman Khandual 详细说明了补丁的更改，包括在 __cpu_setup() 中用 MDSCR_EL1_TDCC 替代开放编码，解决了由于变量类型不匹配导致的构建警告。此外，补丁得到了 Ada Couprie Diaz 的审核通过，表明其已准备好进一步合并。整体来看，补丁系列的目标是简化代码并提高其准确性。

#### 📝 邮件列表

1. **[06-13 08:06]** [PATCH V5 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[06-13 08:06]** [PATCH V5 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[06-13 08:06]** [PATCH V5 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 17: [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Sun, 8 Jun 2025 17:54:02 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下自测的补丁，主要目的是在 `arch_timer_edge_cases` 测试中关闭 GIC（通用中断控制器）文件描述符，以便正确清理虚拟机并消除运行时的警告信息。

在历史讨论中，Zenghui Yu 提出了这个补丁，指出关闭 GIC FD 可以释放其对虚拟机的引用，从而避免出现 "KVM: debugfs: duplicate directory" 的警告。补丁的代码修改涉及到一个文件，增加了 13 行代码并删除了 3 行。

在本周的新讨论中，参与者 Sebastian Ott 和 Miguel Luis 对该补丁进行了审核，并分别表示支持（Reviewed-by），确认补丁的有效性和必要性。这表明补丁得到了积极的反馈，可能会在后续版本中被合并。整体来看，讨论进展顺利，补丁的接受度较高。

#### 📝 邮件列表

1. **[06-08 17:54]** [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[06-10 14:38]** Re: [PATCH] KVM: arm64: selftests: Close the GIC FD in
 arch_timer_edge_cases
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[06-11 09:47]** Re: [PATCH] KVM: arm64: selftests: Close the GIC FD in
 arch_timer_edge_cases
   - 发件人: Miguel Luis <miguel.luis@oracle.com>

---

### Thread 18: [PATCH v2 00/15] Add KVM Selftests runner

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Jun 2025 16:56:04 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 自测试运行器的补丁（PATCH v2 00/15），该补丁旨在增强 KVM 自测试的运行体验。补丁的主要目标包括简化贡献者和维护者运行不同配置测试的过程，提供输出保留、控制输出详细程度、并行执行及命令行参数组合等功能。

在历史讨论中，Vipin Sharma 提出了该补丁的初步版本，并详细描述了其功能和目标。此外，他还提交了针对 RISC-V 平台的自动生成测试文件的补丁（PATCH v2 15/15），以支持 KVM 自测试运行器。

在本周的新讨论中，Andrew Jones 对 Vipin Sharma 的补丁进行了简单的回复，确认了补丁内容的准确性，并表示感谢。这表明补丁得到了积极的关注，但目前尚未有进一步的技术反馈或修改建议。

总体来看，本周的讨论主要是对补丁的确认，尚未涉及深入的技术问题或新的进展。

#### 📝 邮件列表

1. **[06-06 16:56]** [PATCH v2 00/15] Add KVM Selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
2. **[06-06 16:56]** [PATCH v2 15/15] KVM: selftests: Add riscv auto generated test files
 for KVM Selftests Runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
3. **[06-09 14:54]** Re: [PATCH v2 15/15] KVM: selftests: Add riscv auto generated test
 files for KVM Selftests Runner
   - 发件人: Andrew Jones <ajones@ventanamicro.com>

---

### Thread 19: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 14 Jun 2025 22:57:21 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `vgic_v3_put_nested()` 函数中对 `s_cpu_if->vgic_lr[]` 数组的索引问题。

**原始补丁内容**：补丁由 Wei-Lin Chang 提交，主要修正了 `vgic_v3_put_nested()` 函数在访问 `s_cpu_if->vgic_lr[]` 时的索引逻辑。原本该数组是从索引 0 开始连续填充到 `s_cpu_if->used_lrs - 1`，但函数却使用了 `shadow_if->lr_map` 中设置位的位置进行索引，导致潜在的错误。

**之前讨论要点**：由于本邮件线程没有历史讨论，因此没有相关的背景信息。

**本周新讨论与进展**：本周的讨论集中在补丁的具体实现上，Wei-Lin Chang 提供了对 `vgic_v3_put_nested()` 函数的修改，增加了一个 `index` 变量来正确地索引 `s_cpu_if->vgic_lr[]` 数组。补丁中对代码进行了相应的插入和删除，确保在处理虚拟 CPU 的中断路由时，能够正确地清除和更新 `vgic_lr` 的状态。

总的来说，这个补丁解决了 KVM 中 arm64 架构下的一个重要索引错误，确保了虚拟化环境中的中断处理逻辑的正确性。

#### 📝 邮件列表

1. **[06-14 22:57]** [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 20: [PATCH v5 0/6] KVM: lockdep improvements

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 10 Jun 2025 16:28:29 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）的锁依赖性改进，涉及到一系列的补丁（patch）。本周的讨论主要集中在一个补丁系列的应用情况上。

1. **原始补丁内容**：该补丁系列包含六个部分，主要目的是改进 KVM 的锁机制，具体包括实现嵌套的互斥锁尝试锁定、可中断的互斥锁、以及在 KVM 中对所有虚拟 CPU 的锁定操作的改进。

2. **之前讨论要点**：虽然邮件中没有提供详细的历史讨论内容，但可以推测这些补丁是为了提升 KVM 在处理并发操作时的效率和安全性，特别是在多核处理器环境下。

3. **本周的新讨论与进展**：本周的邮件确认了该补丁系列已被应用到 riscv/linux.git 的修复分支中。参与者 Paolo Bonzini 提供了每个补丁的链接，显示了补丁的具体实现和改进。整体来看，这些改进将增强 KVM 的锁管理能力，提升其性能和稳定性。

总结而言，本周的讨论确认了 KVM 锁依赖性改进补丁的成功应用，标志着该项目的进一步进展。

#### 📝 邮件列表

1. **[06-10 16:28]** Re: [PATCH v5 0/6] KVM: lockdep improvements
   - 发件人: patchwork-bot+linux-riscv@kernel.org

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH v2 2/9] KVM: arm64: nv: selftests: Add simple test to
 run guest code in vEL2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 9 Jun 2025 12:14:36 +0900

#### 🤖 AI 总结

本邮件主题为“[RFC PATCH v2 2/9] KVM: arm64: nv: selftests: Add simple test to run guest code in vEL2”，主要讨论在 KVM 的 arm64 架构中增加一个简单的自测试，以便在 vEL2 环境中运行来宾代码。

在历史讨论中，邮件列表并未提供具体的背景信息或之前的讨论内容，因此我们无法获取有关该补丁的详细历史。该补丁的主要目的是增强 KVM 的功能，特别是在嵌套虚拟化的场景下。

在本周的新讨论中，参与者 Ganapatrao Kulkarni 提到该补丁系列是基于最新的 kvmarm-next 内核，并在 QEMU 的 TCG 模式下进行了测试，使用了启动时添加的 kvm-arm.mode=nested 选项。测试结果由 Itaru Kitayama 确认，表明补丁在该环境下运行正常。

总体来看，本周的讨论集中在补丁的测试情况上，确认了其在特定环境下的有效性，为后续的开发和完善提供了积极的反馈。

#### 📝 邮件列表

1. **[06-09 12:14]** Re: [RFC PATCH v2 2/9] KVM: arm64: nv: selftests: Add simple test to
 run guest code in vEL2
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: pkvm boot failures

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 09 Jun 2025 18:53:40 +0530

#### 🤖 AI 总结

本邮件讨论主题为“pkvm 启动失败”，主要围绕在 Linux 内核中使用 pKVM 时遇到的内核崩溃问题。

1. **原始问题**：参与者 Aneesh Kumar K.V 报告了在使用 v6.15 内核时，禁用 CONFIG_PROTECTED_NVHE_STACKTRACE 后，系统出现内核崩溃，崩溃信息显示在 hyp_assert_lock_held() 函数中。

2. **之前讨论要点**：在本周的讨论中，Marc Zyngier 提出，崩溃可能与 S1 转换故障有关，并询问 EL2 试图访问的地址。Mostafa Saleh 进一步分析发现，问题与 CONFIG_JUMP_LABEL=n 配置有关，导致在访问 kvm_protected_mode_initialized 时出现崩溃，因为该变量未在 hypervisor 的命名空间中正确映射。

3. **本周的新讨论与进展**：Mostafa 提出了将 kvm_protected_mode_initialized 变量的定义移动到 hypervisor 命名空间的建议，并提出了相应的代码修改。Aneesh 也指出，其他引用该变量的地方需要更新。Marc 认为应该始终支持 JUMP_LABEL，并建议在 KVM 配置中强制启用该选项。讨论中还提到，未来可能需要添加注释以解释该静态键无法从 hypervisor 读取的原因。

总体来看，邮件讨论集中在如何解决 pKVM 启动失败的根本原因及其配置依赖关系，参与者们积极提出解决方案和代码修改建议。

#### 📝 邮件列表

1. **[06-09 18:53]** pkvm boot failures
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
2. **[06-09 17:24]** Re: pkvm boot failures
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-09 17:25]** Re: pkvm boot failures
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[06-10 12:03]** Re: pkvm boot failures
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
5. **[06-10 08:34]** Re: pkvm boot failures
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[06-10 09:03]** Re: pkvm boot failures
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[06-10 09:06]** Re: pkvm boot failures
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.16, take #2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Jun 2025 10:43:50 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的修复补丁，主要涉及 6.16 版本的第二批修复。

在历史讨论中，Marc Zyngier 提出了这一补丁，强调了对系统寄存器访问器的重大重构，以确保 RES0/RES1 的清理在正确的时机应用。此外，他指出了一些自测试存在的问题，这些测试在之前的版本中几乎从未正常工作。邮件中还提到了一些具体的代码更改，旨在修复这些问题。

在本周的新讨论中，Paolo Bonzini 对 Marc 的补丁表示感谢，并确认已将其合并。这表明补丁得到了认可并成功纳入了代码库。

总结而言，此次讨论的重点是 KVM/arm64 的修复补丁的提交与合并，解决了系统寄存器访问和自测试的问题，推动了 6.16 版本的改进。

#### 📝 邮件列表

1. **[06-06 10:43]** [GIT PULL] KVM/arm64 fixes for 6.16, take #2
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[06-11 20:25]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #2
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

