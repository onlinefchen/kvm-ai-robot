# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 10:17:07

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 263
- **总 Thread 数**: 31
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 30 threads (259 邮件)
- **RFC**: 1 threads (4 邮件)

---

## 📌 PATCH

共 30 个 thread

---

### Thread 1: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 67 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 16 Apr 2025 14:41:22 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 中对 Arm CCA（保密计算架构）支持的补丁系列（PATCH v8 00/43）。该补丁旨在为 KVM 提供保护虚拟机的能力，相关的来宾支持已在 v6.14-rc1 中合并。

在历史讨论中，补丁的主要内容包括增加了新的 ioctl 和能力的文档，添加了对 RME（Realm Management Extension）支持的检查，以及定义用户 ABI 的初步补丁等。这些补丁经过多次修改，逐步完善了对 Realm 和 REC（Realm Execution Context）的创建和配置支持。

本周的新讨论主要集中在对补丁的细节审查上。参与者对补丁中的一些小问题（如命名、文档表述等）提出了建议和修改意见。例如，Suzuki K Poulose 提出了对某些参数的命名和文档的改进建议，Gavin Shan 则关注了补丁中对 VCPU 创建和激活的逻辑是否清晰，确保在 Realm 激活后不允许再添加 VCPU。

总体来看，本周的讨论进一步推动了补丁的完善，参与者们积极反馈并确认了多个补丁的审查结果，为最终合并做好准备。

#### 📝 邮件列表

1. **[04-16 14:41]** [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[04-16 14:41]** [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
3. **[04-16 14:41]** [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
4. **[04-16 14:41]** [PATCH v8 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
5. **[04-16 14:41]** [PATCH v8 08/43] kvm: arm64: Don't expose debug capabilities for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
6. **[04-16 14:41]** [PATCH v8 09/43] KVM: arm64: Allow passing machine type in KVM creation
   - 发件人: Steven Price <steven.price@arm.com>
7. **[04-16 14:41]** [PATCH v8 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
8. **[04-16 14:41]** [PATCH v8 12/43] KVM: arm64: vgic: Provide helper for number of list registers
   - 发件人: Steven Price <steven.price@arm.com>
9. **[04-16 14:41]** [PATCH v8 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
10. **[04-16 14:41]** [PATCH v8 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
11. **[04-16 14:41]** [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
12. **[04-16 14:41]** [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
13. **[04-16 14:41]** [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
14. **[04-16 14:41]** [PATCH v8 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
15. **[04-16 14:41]** [PATCH v8 22/43] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
16. **[04-16 14:41]** [PATCH v8 27/43] arm64: RME: support RSI_HOST_CALL
   - 发件人: Steven Price <steven.price@arm.com>
17. **[04-16 14:41]** [PATCH v8 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Steven Price <steven.price@arm.com>
18. **[04-16 14:41]** [PATCH v8 33/43] arm64: RME: Hide KVM_CAP_READONLY_MEM for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
19. **[04-16 14:41]** [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and watchpoints to userspace
   - 发件人: Steven Price <steven.price@arm.com>
20. **[04-16 14:41]** [PATCH v8 36/43] arm64: RME: Initialize PMCR.N with number counter supported by RMM
   - 发件人: Steven Price <steven.price@arm.com>
21. **[04-16 14:41]** [PATCH v8 37/43] arm64: RME: Propagate max SVE vector length from RMM
   - 发件人: Steven Price <steven.price@arm.com>
22. **[04-16 14:42]** [PATCH v8 38/43] arm64: RME: Configure max SVE vector length for a Realm
   - 发件人: Steven Price <steven.price@arm.com>
23. **[04-16 14:42]** [PATCH v8 39/43] arm64: RME: Provide register list for unfinalized RME RECs
   - 发件人: Steven Price <steven.price@arm.com>
24. **[04-16 14:42]** [PATCH v8 40/43] arm64: RME: Provide accurate register list
   - 发件人: Steven Price <steven.price@arm.com>
25. **[04-16 14:42]** [PATCH v8 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>
26. **[04-16 14:42]** [PATCH v8 42/43] KVM: arm64: Expose KVM_ARM_VCPU_REC to user space
   - 发件人: Steven Price <steven.price@arm.com>
27. **[04-16 14:42]** [PATCH v8 43/43] KVM: arm64: Allow activating realms
   - 发件人: Steven Price <steven.price@arm.com>
28. **[04-25 12:08]** Re: [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
29. **[04-28 09:58]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
30. **[04-29 10:45]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
31. **[04-30 14:25]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Gavin Shan <gshan@redhat.com>
32. **[04-30 15:39]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Gavin Shan <gshan@redhat.com>
33. **[04-30 15:42]** Re: [PATCH v8 08/43] kvm: arm64: Don't expose debug capabilities for
 realm guests
   - 发件人: Gavin Shan <gshan@redhat.com>
34. **[04-30 15:47]** Re: [PATCH v8 09/43] KVM: arm64: Allow passing machine type in KVM
 creation
   - 发件人: Gavin Shan <gshan@redhat.com>
35. **[04-30 15:54]** Re: [PATCH v8 12/43] KVM: arm64: vgic: Provide helper for number of
 list registers
   - 发件人: Gavin Shan <gshan@redhat.com>
36. **[04-30 21:38]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
37. **[04-30 21:55]** Re: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Gavin Shan <gshan@redhat.com>
38. **[04-30 22:11]** Re: [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Gavin Shan <gshan@redhat.com>
39. **[05-01 10:16]** Re: [PATCH v8 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
40. **[05-01 12:54]** Re: [PATCH v8 22/43] KVM: arm64: Validate register access for a Realm
 VM
   - 发件人: Gavin Shan <gshan@redhat.com>
41. **[05-01 12:57]** Re: [PATCH v8 27/43] arm64: RME: support RSI_HOST_CALL
   - 发件人: Gavin Shan <gshan@redhat.com>
42. **[05-01 12:59]** Re: [PATCH v8 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Gavin Shan <gshan@redhat.com>
43. **[05-01 13:01]** Re: [PATCH v8 33/43] arm64: RME: Hide KVM_CAP_READONLY_MEM for realm
 guests
   - 发件人: Gavin Shan <gshan@redhat.com>
44. **[05-01 13:04]** Re: [PATCH v8 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Gavin Shan <gshan@redhat.com>
45. **[05-01 13:04]** Re: [PATCH v8 42/43] KVM: arm64: Expose KVM_ARM_VCPU_REC to user
 space
   - 发件人: Gavin Shan <gshan@redhat.com>
46. **[05-01 13:06]** Re: [PATCH v8 43/43] KVM: arm64: Allow activating realms
   - 发件人: Gavin Shan <gshan@redhat.com>
47. **[05-01 13:36]** Re: [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
48. **[05-01 13:40]** Re: [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
49. **[05-01 13:40]** Re: [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
50. **[05-01 13:42]** Re: [PATCH v8 36/43] arm64: RME: Initialize PMCR.N with number
 counter supported by RMM
   - 发件人: Gavin Shan <gshan@redhat.com>
51. **[05-01 13:50]** Re: [PATCH v8 37/43] arm64: RME: Propagate max SVE vector length from
 RMM
   - 发件人: Gavin Shan <gshan@redhat.com>
52. **[05-01 13:50]** Re: [PATCH v8 38/43] arm64: RME: Configure max SVE vector length for
 a Realm
   - 发件人: Gavin Shan <gshan@redhat.com>
53. **[05-01 14:31]** Re: [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
54. **[05-01 14:31]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
55. **[05-01 14:44]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
56. **[05-01 14:47]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
57. **[05-01 16:09]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Steven Price <steven.price@arm.com>
58. **[05-01 16:11]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Steven Price <steven.price@arm.com>
59. **[05-01 17:00]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
60. **[05-01 17:50]** Re: [PATCH v8 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
61. **[05-01 17:51]** Re: [PATCH v8 12/43] KVM: arm64: vgic: Provide helper for number of
 list registers
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
62. **[05-02 09:30]** Re: [PATCH v8 39/43] arm64: RME: Provide register list for
 unfinalized RME RECs
   - 发件人: Gavin Shan <gshan@redhat.com>
63. **[05-02 09:41]** Re: [PATCH v8 40/43] arm64: RME: Provide accurate register list
   - 发件人: Gavin Shan <gshan@redhat.com>
64. **[05-02 09:59]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
65. **[05-02 10:46]** Re: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>
66. **[05-02 12:04]** Re: [PATCH v8 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
67. **[05-02 13:22]** Re: [PATCH v8 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 2: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling

**📧 邮件数**: 44 | **👥 参与者**: 4 | **📅 开始时间**: Sat, 26 Apr 2025 13:27:54 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的细粒度陷阱（Fine Grained Trap，FGT）处理的修订，主要集中在一系列补丁（PATCH v3 00/42）上。

1. **原始补丁内容**：该补丁系列旨在重构 KVM 的细粒度陷阱处理，增加对新特性的支持，特别是与 FEAT_LS64 和 FGT2 相关的系统寄存器的处理。补丁的数量从之前的版本增加了一倍，涵盖了大量的代码更改和新功能的实现。

2. **之前讨论要点**：历史讨论中，Marc Zyngier 提到补丁的紧迫性，并详细描述了补丁的变化，特别是对系统寄存器的更新和新寄存器的添加。讨论中还提到了一些潜在的错误和设计决策的合理性。

3. **本周新讨论及进展**：本周的讨论主要集中在补丁合并后的测试结果上。Ganapatrao Kulkarni 报告了在运行自测时遇到的问题，Marc Zyngier 对此进行了深入分析，指出了测试代码中的缺陷，并提出了改进建议。此外，Ben Horgan 和 Joey Gouly 也对补丁中的小错误和代码风格提出了反馈，并确认了一些补丁的审核通过。整体来看，讨论显示出对补丁的积极推进和对现有问题的持续关注。

总结而言，本周的讨论不仅推动了补丁的完善，也反映了开发者们对 KVM ARM64 细粒度陷阱处理的深入理解和协作精神。

#### 📝 邮件列表

1. **[04-26 13:27]** [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-26 13:27]** [PATCH v3 01/42] arm64: sysreg: Add ID_AA64ISAR1_EL1.LS64 encoding for FEAT_LS64WB
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-26 13:27]** [PATCH v3 02/42] arm64: sysreg: Update ID_AA64MMFR4_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-26 13:27]** [PATCH v3 03/42] arm64: sysreg: Add layout for HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-26 13:27]** [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with HFG{R,W}TR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-26 13:28]** [PATCH v3 08/42] arm64: sysreg: Add registers trapped by HFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-26 13:28]** [PATCH v3 09/42] arm64: sysreg: Add registers trapped by HDFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-26 13:28]** [PATCH v3 13/42] arm64: Add syndrome information for trapped LD64B/ST64B{,V,V0}
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-26 13:28]** [PATCH v3 16/42] KVM: arm64: Simplify handling of negative FGT bits
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-26 13:28]** [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-26 13:28]** [PATCH v3 18/42] KVM: arm64: Restrict ACCDATA_EL1 undef to FEAT_ST64_ACCDATA being disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-26 13:28]** [PATCH v3 21/42] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-26 13:28]** [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-26 13:28]** [PATCH v3 28/42] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[04-26 13:28]** [PATCH v3 40/42] KVM: arm64: Allow sysreg ranges for FGT descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[04-26 13:28]** [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[04-29 00:03]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
18. **[04-28 22:42]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[04-29 08:34]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[04-29 14:07]** Re: [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with
 HFG{R,W}TR_EL2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[04-29 14:07]** Re: [PATCH v3 09/42] arm64: sysreg: Add registers trapped by
 HDFG{R,W}TR2_EL2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
22. **[04-29 14:08]** Re: [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64*
 instructions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[04-29 14:08]** Re: [PATCH v3 18/42] KVM: arm64: Restrict ACCDATA_EL1 undef to
 FEAT_ST64_ACCDATA being disabled
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[04-29 14:08]** Re: [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain
 traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[04-29 14:08]** Re: [PATCH v3 40/42] KVM: arm64: Allow sysreg ranges for FGT
 descriptors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
26. **[04-29 14:09]** Re: [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[04-29 14:34]** Re: [PATCH v3 01/42] arm64: sysreg: Add ID_AA64ISAR1_EL1.LS64
 encoding for FEAT_LS64WB
   - 发件人: Joey Gouly <joey.gouly@arm.com>
28. **[04-29 14:38]** Re: [PATCH v3 02/42] arm64: sysreg: Update ID_AA64MMFR4_EL1
 description
   - 发件人: Joey Gouly <joey.gouly@arm.com>
29. **[04-29 14:49]** Re: [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[04-29 15:02]** Re: [PATCH v3 03/42] arm64: sysreg: Add layout for HCR_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
31. **[04-29 15:09]** Re: [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain
 traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
32. **[04-29 15:10]** Re: [PATCH v3 09/42] arm64: sysreg: Add registers trapped by HDFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[04-29 15:26]** Re: [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with
 HFG{R,W}TR_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
34. **[04-29 20:00]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
35. **[04-29 15:30]** Re: [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[05-01 11:11]** Re: [PATCH v3 08/42] arm64: sysreg: Add registers trapped by
 HFG{R,W}TR2_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
37. **[05-01 11:17]** Re: [PATCH v3 13/42] arm64: Add syndrome information for trapped
 LD64B/ST64B{,V,V0}
   - 发件人: Joey Gouly <joey.gouly@arm.com>
38. **[05-01 11:43]** Re: [PATCH v3 16/42] KVM: arm64: Simplify handling of negative FGT
 bits
   - 发件人: Joey Gouly <joey.gouly@arm.com>
39. **[05-01 12:01]** Re: [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64*
 instructions
   - 发件人: Joey Gouly <joey.gouly@arm.com>
40. **[05-01 12:32]** Re: [PATCH v3 21/42] KVM: arm64: Compute FGT masks from KVM's own
 FGT tables
   - 发件人: Joey Gouly <joey.gouly@arm.com>
41. **[05-01 14:20]** Re: [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with HFG{R,W}TR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[05-01 14:33]** Re: [PATCH v3 28/42] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Joey Gouly <joey.gouly@arm.com>
43. **[05-01 14:46]** Re: [PATCH v3 08/42] arm64: sysreg: Add registers trapped by HFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
44. **[05-01 14:52]** Re: [PATCH v3 08/42] arm64: sysreg: Add registers trapped by
 HFG{R,W}TR2_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 3: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags

**📧 邮件数**: 18 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 16 Apr 2025 08:51:05 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构下允许使用 VMA（虚拟内存区域）标志进行可缓存的二级映射的补丁（PATCH v3 1/1）。该补丁旨在解决在没有 FWB（写后无效）支持的情况下，用户空间对可缓存 PFNMAP（页面框架号映射）的处理问题。

在历史讨论中，参与者们探讨了 KVM 是否需要一个能力标志（KVM_CAP）来指示内核是否支持可缓存的 PFNMAP。大多数人认为，虽然这个能力标志有其价值，但 memslot 标志并不是必需的，因为它无法影响 KVM 的代码逻辑。讨论还涉及了如何防止在不支持 FWB 的情况下创建可缓存的 PFNMAP。

本周的新讨论中，Ankit Agrawal 提出了具体的实现步骤，包括在 memslot 创建时阻止可缓存的 PFNMAP，并在 S2FWB 启用时支持可缓存的 PFNMAP。他还建议将 VFIO 和 KVM 之间的通信路径分开。Catalin Marinas 和 Jason Gunthorpe 进一步讨论了可执行映射的处理，以及是否需要为可执行 PFNMAP 引入新的能力标志。总体而言，讨论集中在如何确保 KVM 在处理可缓存映射时的安全性和一致性。

#### 📝 邮件列表

1. **[04-16 08:51]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
2. **[04-22 00:49]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[04-22 10:54]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
4. **[04-22 17:50]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[04-22 14:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
6. **[04-22 14:28]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[04-22 20:35]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
8. **[04-23 11:45]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[04-23 09:02]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
10. **[04-23 13:26]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[04-23 10:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
12. **[04-29 10:47]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
13. **[04-29 14:27]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
14. **[04-29 11:14]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
15. **[04-29 17:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
16. **[04-29 13:44]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
17. **[04-29 19:09]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
18. **[04-29 15:19]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>

---

### Thread 4: [PATCH v4 0/5] KVM: lockdep improvements

**📧 邮件数**: 14 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 30 Apr 2025 16:30:08 -0400

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）锁依赖性（lockdep）改进的补丁系列，主要集中在如何有效地锁定所有虚拟 CPU（vCPUs）以避免在高并发情况下触发锁依赖性警告。

1. **原始补丁内容**：补丁系列（PATCH v4 0/5）旨在实现锁依赖性的改进，特别是通过引入 `mutex_trylock_nest_lock()` 和 `mutex_lock_killable_nest_lock()` 函数，来优化 KVM 中对所有 vCPUs 的锁定操作。

2. **之前讨论要点**：历史讨论中提到，现有的锁定方法在处理大量 vCPUs（如超过 48 个）时，容易导致 lockdep 报告错误，进而禁用锁定正确性验证。补丁通过使用嵌套锁的特性来解决这一问题，减少了重复代码。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现和细节上。参与者对补丁的结构、命名和功能提出了建议和质疑，尤其是关于锁定操作的必要性和性能影响。Maxim Levitsky 继续推进补丁的修改，其他参与者如 Marc Zyngier 和 Peter Zijlstra 也提供了反馈，讨论了不同架构的实现差异以及是否需要在新函数中添加断言。最终，补丁的目标是确保在高并发情况下的锁定操作不会引发错误，同时保持代码的可读性和一致性。

#### 📝 邮件列表

1. **[04-30 16:30]** [PATCH v4 0/5] KVM: lockdep improvements
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
2. **[04-30 16:30]** [PATCH v4 1/5] locking/mutex: implement mutex_trylock_nested
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
3. **[04-30 16:30]** [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
4. **[04-30 16:30]** [PATCH v4 3/5] RISC-V: KVM: switch to kvm_trylock/unlock_all_vcpus
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
5. **[04-30 16:30]** [PATCH v4 4/5] locking/mutex: implement mutex_lock_killable_nest_lock
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
6. **[04-30 16:30]** [PATCH v4 5/5] x86: KVM: SEV: implement kvm_lock_all_vcpus and use it
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
7. **[05-01 09:24]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-01 13:15]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when
 locking all vCPUs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
9. **[05-01 13:44]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[05-01 15:41]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when
 locking all vCPUs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
11. **[05-01 14:55]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[05-02 13:57]** Re: [PATCH v4 5/5] x86: KVM: SEV: implement kvm_lock_all_vcpus and
 use it
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[05-02 13:58]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when
 locking all vCPUs
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[05-03 12:08]** Re: [PATCH v4 5/5] x86: KVM: SEV: implement kvm_lock_all_vcpus and
 use it
   - 发件人: Peter Zijlstra <peterz@infradead.org>

---

### Thread 5: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36

**📧 邮件数**: 14 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 15 Apr 2025 08:47:10 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对AmpereOne处理器的错误AC03_CPU_36的补丁及其相关问题。补丁的主要内容是通过在写入HCR_EL2寄存器时屏蔽异步异常，来避免在处理器状态更新时可能出现的异常路由错误。D Scott Phillips提出了该补丁，并在后续讨论中，Marc Zyngier确认了补丁的有效性，指出在nVHE模式下该错误不会发生，因此补丁的适用性得到了进一步确认。

在历史讨论中，参与者们探讨了该错误的具体表现及其影响，Marc Zyngier提出了对nVHE模式的考虑，认为在该模式下异步异常始终被屏蔽，因此不会触发该错误。

本周的新讨论中，Marc Zyngier继续推进补丁的实施，并提出了与KVM相关的其他补丁，旨在解决AArch64支持的管理问题，确保用户空间无法禁用AArch64支持。此外，他还提出了对HCRX_EL2寄存器的正确保存和恢复的补丁，以解决在虚拟机退出时寄存器值丢失的问题。Ganapatrao Kulkarni对这些补丁表示了支持，并进行了审核。整体来看，讨论集中在确保补丁的有效性及其对系统稳定性的影响上。

#### 📝 邮件列表

1. **[04-15 08:47]** [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
2. **[04-16 08:19]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-24 19:02]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum
 AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
4. **[04-27 13:21]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-28 09:35]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum
 AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
6. **[04-29 12:41]** [PATCH 0/2] KVM: arm64: Make AArch64 support sticky
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-29 12:41]** [PATCH 1/2] KVM: arm64: Prevent userspace from disabling AArch64 support at any virtualisable EL
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-29 12:41]** [PATCH 2/2] KVM: arm64: selftest: Don't try to disable AArch64 support
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-30 11:08]** Re: [PATCH 0/2] KVM: arm64: Make AArch64 support sticky
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
10. **[04-30 11:59]** [PATCH 0/2] KVM: arm64: Fix HCRX_EL2.GCSEn handling
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-30 11:59]** [PATCH 1/2] KVM: arm64: Properly save/restore HCRX_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-30 11:59]** [PATCH 2/2] KVM: arm64: Kill HCRX_HOST_FLAGS
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-30 10:01]** Re: [PATCH 1/2] KVM: selftests: Add default testfiles for KVM
 selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[04-30 14:31]** Re: [PATCH 2/2] KVM: selftests: Create KVM selftest runner
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 6: [PATCH 00/10] KVM: selftests: Convert to kernel-style types

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  1 May 2025 11:32:54 -0700

#### 🤖 AI 总结

[AI 总结失败: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 220417 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}]
策略: 完整 thread (历史:0 新:13, 182916 tokens)

#### 📝 邮件列表

1. **[05-01 11:32]** [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: David Matlack <dmatlack@google.com>
2. **[05-01 11:32]** [PATCH 01/10] KVM: selftests: Use gva_t instead of vm_vaddr_t
   - 发件人: David Matlack <dmatlack@google.com>
3. **[05-01 11:32]** [PATCH 02/10] KVM: selftests: Use gpa_t instead of vm_paddr_t
   - 发件人: David Matlack <dmatlack@google.com>
4. **[05-01 11:32]** [PATCH 03/10] KVM: selftests: Use gpa_t for GPAs in Hyper-V selftests
   - 发件人: David Matlack <dmatlack@google.com>
5. **[05-01 11:32]** [PATCH 04/10] KVM: selftests: Use u64 instead of uint64_t
   - 发件人: David Matlack <dmatlack@google.com>
6. **[05-01 11:32]** [PATCH 05/10] KVM: selftests: Use s64 instead of int64_t
   - 发件人: David Matlack <dmatlack@google.com>
7. **[05-01 11:33]** [PATCH 06/10] KVM: selftests: Use u32 instead of uint32_t
   - 发件人: David Matlack <dmatlack@google.com>
8. **[05-01 11:33]** [PATCH 07/10] KVM: selftests: Use s32 instead of int32_t
   - 发件人: David Matlack <dmatlack@google.com>
9. **[05-01 11:33]** [PATCH 08/10] KVM: selftests: Use u16 instead of uint16_t
   - 发件人: David Matlack <dmatlack@google.com>
10. **[05-01 11:33]** [PATCH 09/10] KVM: selftests: Use s16 instead of int16_t
   - 发件人: David Matlack <dmatlack@google.com>
11. **[05-01 11:33]** [PATCH 10/10] KVM: selftests: Use u8 instead of uint8_t
   - 发件人: David Matlack <dmatlack@google.com>
12. **[05-01 14:03]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[05-02 11:11]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: Andrew Jones <ajones@ventanamicro.com>

---

### Thread 7: [PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 14:07:31 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 平台的 Hyper-V 支持的补丁系列，主题为“支持虚拟信任级别启动（Virtual Trust Level Boot）”。该补丁集包含 11 个补丁，旨在使 Hyper-V 代码能够在 ARM64 上的虚拟信任级别下启动。

**原始补丁内容**：补丁系列的核心是允许 Hyper-V 在 ARM64 环境中支持虚拟信任级别启动，涉及到对 VTL 模式的实现和相关驱动的修改。

**之前讨论要点**：在补丁的早期版本中，开发者 Roman Kisel 进行了多次迭代，逐步调整代码以解决编译警告、优化代码结构，并确保与现有的 KVM 和 ACPI 兼容性。补丁的功能性变化较少，主要集中在代码的清晰度和可维护性上。

**本周新讨论与进展**：本周的讨论主要集中在补丁的具体实现上，包括：
1. 通过 SMCCC 检测 Hyper-V 的存在。
2. 更新 Kconfig 以支持 ARM64 的 VTL 模式。
3. 初始化 VTL 字段以确保 VMBus 能够正确通信。
4. 增加对设备树的支持，以便在 VTL 模式下获取 IRQ 配置。
5. 引入新的 API 以获取 VMBus 根设备。

整体来看，该补丁系列的进展顺利，得到了多位开发者的认可和支持，预计将为 ARM64 平台的 Hyper-V 提供更好的功能支持。

#### 📝 邮件列表

1. **[04-28 14:07]** [PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[04-28 14:07]** [PATCH hyperv-next v9 01/11] arm64: kvm, smccc: Introduce and use API for getting hypervisor UUID
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
3. **[04-28 14:07]** [PATCH hyperv-next v9 02/11] arm64: hyperv: Use SMCCC to detect hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
4. **[04-28 14:07]** [PATCH hyperv-next v9 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
5. **[04-28 14:07]** [PATCH hyperv-next v9 04/11] Drivers: hv: Provide arch-neutral implementation of get_vtl()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
6. **[04-28 14:07]** [PATCH hyperv-next v9 05/11] arm64: hyperv: Initialize the Virtual Trust Level field
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[04-28 14:07]** [PATCH hyperv-next v9 06/11] arm64, x86: hyperv: Report the VTL the system boots in
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
8. **[04-28 14:07]** [PATCH hyperv-next v9 07/11] dt-bindings: microsoft,vmbus: Add interrupt and DMA coherence properties
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
9. **[04-28 14:07]** [PATCH hyperv-next v9 08/11] Drivers: hv: vmbus: Get the IRQ number from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
10. **[04-28 14:07]** [PATCH hyperv-next v9 09/11] Drivers: hv: vmbus: Introduce hv_get_vmbus_root_device()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
11. **[04-28 14:07]** [PATCH hyperv-next v9 10/11] ACPI: irq: Introduce acpi_get_gsi_dispatcher()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
12. **[04-28 14:07]** [PATCH hyperv-next v9 11/11] PCI: hv: Get vPCI MSI IRQ domain from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
13. **[05-02 04:08]** RE: [PATCH hyperv-next v9 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Michael Kelley <mhklinux@outlook.com>

---

### Thread 8: [PATCH 0/3] Two minor fixups around FEAT_E2H0

**📧 邮件数**: 12 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 29 Apr 2025 21:27:53 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A（Firmware Framework for Arm）1.2 及 SEND_DIRECT2 ABI 的一系列补丁。

1. **原始补丁内容**：本次补丁集包含三部分，主要目的是为了支持 FF-A 1.2 规范中引入的新 SEND_DIRECT2 ABI，该 ABI 允许使用寄存器 x4-x17 作为消息载荷。补丁还防止主机使用低于已与虚拟机监控器协商的 FF-A 版本。

2. **之前讨论要点**：在历史讨论中，参与者讨论了 FF-A 1.2 的兼容性问题，特别是 FF-A 1.1 版本对 ABI 的破坏，以及如何处理主机与虚拟机监控器之间的版本协商问题。

3. **本周新讨论与进展**：本周的讨论中，Per Larsen 提交了补丁并确认已成功在 QEMU 上测试运行 Android 和 Trusty。邮件中还提到补丁的格式问题，Marc Zyngier 指出补丁的发送格式不当，并询问作者信息。其他参与者建议在补丁系列中标记版本号，并附上变更日志。整体来看，补丁的开发和测试进展顺利，但在邮件格式和文档方面存在改进空间。

#### 📝 邮件列表

1. **[04-29 21:27]** Re: [PATCH 0/3] Two minor fixups around FEAT_E2H0
   - 发件人: Will Deacon <will@kernel.org>
2. **[05-01 20:49]** [PATCH 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen <perl@immunant.com>
3. **[05-01 20:52]** [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Per Larsen <perl@immunant.com>
4. **[05-01 20:53]** [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Per Larsen <perl@immunant.com>
5. **[05-01 20:55]** [PATCH 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in host handler
   - 发件人: Per Larsen <perl@immunant.com>
6. **[05-02 09:47]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[05-02 09:49]** Re: [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-02 02:21]** [PATCH 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen <perl@immunant.com>
9. **[05-02 02:21]** [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Per Larsen <perl@immunant.com>
10. **[05-02 02:21]** [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Per Larsen <perl@immunant.com>
11. **[05-02 02:21]** [PATCH 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in host handler
   - 发件人: Per Larsen <perl@immunant.com>
12. **[05-02 10:35]** Re: [PATCH 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Sebastian Ene <sebastianene@google.com>

---

### Thread 9: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Apr 2025 16:27:07 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 架构中实现 UBSAN（未定义行为检测器）功能的补丁集。补丁集包含四个部分，旨在为 EL2 模式下的 KVM 代码启用 UBSAN 支持。

历史讨论部分未提供，但本周的新讨论中，Mostafa Saleh 提出了补丁的具体内容。补丁集的主要内容包括：
1. **补丁内容**：补丁集为 EL2 模式引入了 UBSAN 支持，提供两种运行模式：正常模式和陷阱模式。由于 EL2 环境无法打印报告，补丁选择在检测到错误时触发一个“brk”异常。
2. **之前讨论要点**：补丁集的设计考虑了与内核的兼容性，并重用了内核中处理 UBSAN 错误的逻辑，以确保在 KVM 中的错误报告格式一致。
3. **本周新讨论和进展**：Mostafa 提交了补丁并获得了 Kees Cook 的认可，确认补丁的机械性修改和逻辑是正确的。Kees Cook 还提到希望通过硬化树（hardening tree）合并这些补丁，但也考虑到 arm64 团队可能希望通过他们的树来处理此事。

总的来说，本周的讨论集中在补丁的具体实现及其对现有代码的影响上，参与者对补丁的方向表示支持。

#### 📝 邮件列表

1. **[04-30 16:27]** [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[04-30 16:27]** [PATCH v2 1/4] arm64: Introduce esr_is_ubsan_brk()
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[04-30 16:27]** [PATCH v2 2/4] ubsan: Remove regs from report_ubsan_failure()
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[04-30 16:27]** [PATCH v2 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[04-30 16:27]** [PATCH v2 4/4] KVM: arm64: Handle UBSAN faults
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[04-30 11:30]** Re: [PATCH v2 1/4] arm64: Introduce esr_is_ubsan_brk()
   - 发件人: Kees Cook <kees@kernel.org>
7. **[04-30 11:30]** Re: [PATCH v2 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Kees Cook <kees@kernel.org>
8. **[04-30 11:31]** Re: [PATCH v2 4/4] KVM: arm64: Handle UBSAN faults
   - 发件人: Kees Cook <kees@kernel.org>
9. **[04-30 11:32]** Re: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 10: [PATCH hyperv-next v8 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 15:47:02 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持在 ARM64 上的 Hyper-V 中引导虚拟信任级别（Virtual Trust Level Boot）的补丁集。该补丁集旨在使 Hyper-V 代码能够在 ARM64 架构下运行虚拟安全模式，并提供了相关的实现和验证信息。

在历史讨论中，Roman Kisel 提出了多个补丁，包括使用 SMCCC 检测 Hypervisor 存在的补丁和更新 PCI 驱动以支持从设备树获取 vPCI MSI IRQ 域的补丁。Michael Kelley 对这些补丁进行了审查，并提出了一些建议，如将 UUID 定义集中到头文件中，以便于维护。

在本周的新讨论中，Roman Kisel 针对 Michael Kelley 的建议进行了回应，解释了为什么在 Hyper-V 的情况下将 UUID 嵌入函数中更为经济，并表示将会修复之前提到的构建错误。总体来看，讨论持续围绕补丁的实现细节和代码结构优化展开，参与者积极交流以推动补丁的完善。

#### 📝 邮件列表

1. **[04-14 15:47]** [PATCH hyperv-next v8 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[04-14 15:47]** [PATCH hyperv-next v8 02/11] arm64: hyperv: Use SMCCC to detect hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
3. **[04-14 15:47]** [PATCH hyperv-next v8 11/11] PCI: hv: Get vPCI MSI IRQ domain from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
4. **[04-17 15:27]** RE: [PATCH hyperv-next v8 02/11] arm64: hyperv: Use SMCCC to detect
 hypervisor presence
   - 发件人: Michael Kelley <mhklinux@outlook.com>
5. **[04-17 15:28]** RE: [PATCH hyperv-next v8 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Michael Kelley <mhklinux@outlook.com>
6. **[04-28 12:23]** Re: [PATCH hyperv-next v8 02/11] arm64: hyperv: Use SMCCC to detect
 hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[04-28 12:24]** Re: [PATCH hyperv-next v8 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>

---

### Thread 11: [PATCH v3 0/4] KVM: lockdep improvements

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Apr 2025 16:23:07 -0400

#### 🤖 AI 总结

本邮件讨论主题为「KVM: lockdep 改进」，主要涉及对 KVM 虚拟化环境中锁定机制的优化。原始的 patch 系列旨在通过引入 lockdep 的「nest_lock」特性，改善对所有虚拟 CPU（vCPU）的锁定方式，以消除在 SEV 代码中出现的锁定正确性警告。

在历史讨论中，参与者提到需要解决在多个 vCPU 锁定时可能引发的锁定深度问题，尤其是在 ARM 和 RISC-V 架构下。之前的实现存在重复代码和潜在的锁定错误。

本周的新讨论中，Maxim Levitsky 提出了四个具体的 patch：
1. 引入 `mutex_trylock_nest_lock` 和 `mutex_lock_killable_nest_lock` 函数，优化对所有 vCPU 的锁定逻辑。
2. 将 RISC-V 的锁定实现替换为新的 `kvm_trylock_all_vcpus` 和 `kvm_unlock_all_vcpus` 函数，以避免触发锁定警告。
3. 实现 `mutex_lock_killable_nest_lock`，以支持在迁移过程中锁定所有 vCPU。
4. 在 x86 架构下实现 `kvm_lock_all_vcpus`，替代 SEV 的旧锁定方法。

这些改进不仅消除了警告，还减少了代码重复，提高了锁定机制的整体效率。参与者一致认为这些改进是必要的，并期待进一步的测试和反馈。

#### 📝 邮件列表

1. **[04-30 16:23]** [PATCH v3 0/4] KVM: lockdep improvements
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
2. **[04-30 16:23]** [PATCH v3 1/4] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
3. **[04-30 16:23]** [PATCH v3 2/4] RISC-V: KVM: switch to kvm_lock/unlock_all_vcpus
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
4. **[04-30 16:23]** [PATCH v3 3/4] locking/mutex: implement mutex_lock_killable_nest_lock
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
5. **[04-30 16:23]** [PATCH v3 4/4] x86: KVM: SEV: implement kvm_lock_all_vcpus and use it
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
6. **[04-30 16:30]** Re: [PATCH v3 0/4] KVM: lockdep improvements
   - 发件人: mlevitsk@redhat.com

---

### Thread 12: [PATCH RFC 0/4] stackleak: Support Clang stack depth tracking

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  2 May 2025 12:01:23 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Linux 内核的补丁系列，主题为「stackleak: 支持 Clang 堆栈深度跟踪」。该补丁旨在将 Clang 的堆栈深度跟踪功能集成到现有的 stackleak 特性中，以替代 GCC 插件。

**原始补丁/问题内容**：
补丁系列包括四个部分，主要涉及对 stackleak 功能的改进和 Clang 堆栈深度跟踪的支持。补丁中将原有的 `CONFIG_GCC_PLUGIN_STACKLEAK` 重命名为 `CONFIG_STACKLEAK`，并且将跟踪堆栈的函数名从 `stackleak_track_stack` 修改为 `__sanitizer_cov_stack_depth`，以符合 Clang 的命名规范。

**之前讨论要点**：
在之前的讨论中，参与者探讨了如何将 GCC 插件替换为 Clang 实现，强调了 Clang 提供的堆栈深度跟踪回调的潜力。这一改进将提升内核的安全性，减少堆栈泄漏的风险。

**本周的新讨论、进展或结论**：
本周的讨论中，Kees Cook 提出了补丁的具体实现细节，包括将 stackleak 特定的编译标志从 GCC 插件中分离出来，并为 Clang 的堆栈深度跟踪功能配置新的编译选项。此外，补丁还确保在不支持的上下文中不会执行回调。整体来看，本周的进展表明该补丁系列朝着整合 Clang 功能的方向稳步推进。

#### 📝 邮件列表

1. **[05-02 12:01]** [PATCH RFC 0/4] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>
2. **[05-02 12:01]** [PATCH RFC 1/4] stackleak: Rename CONFIG_GCC_PLUGIN_STACKLEAK to CONFIG_STACKLEAK
   - 发件人: Kees Cook <kees@kernel.org>
3. **[05-02 12:01]** [PATCH RFC 2/4] stackleak: Rename stackleak_track_stack to __sanitizer_cov_stack_depth
   - 发件人: Kees Cook <kees@kernel.org>
4. **[05-02 12:01]** [PATCH RFC 3/4] stackleak: Split STACKLEAK_CFLAGS from GCC_PLUGINS_CFLAGS
   - 发件人: Kees Cook <kees@kernel.org>
5. **[05-02 12:01]** [PATCH RFC 4/4] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 13: [PATCH v3 00/10] kvm/arm: Introduce a customizable aarch64 KVM host model

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 18:38:39 +0200

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 ARM 架构下的可定制化 AArch64 主机模型的补丁系列（PATCH v3 00/10）。该补丁旨在通过命令行直接配置 ID 寄存器，主要改进包括将 ID 寄存器存储的重构分离出来，并在此基础上进行重整，改进了文档并修复了一些错误。

在历史讨论中，Cornelia Huck 提出了补丁的背景和主要变更，强调了对 ID 寄存器的可配置性和相关访问器的实现。这些补丁为 ARM CPU 的可写 ID 寄存器提供了访问器，并进行了不同索引之间的转换。

在本周的新讨论中，Sebastian Ott 对补丁中的某些内容提出了建议，指出 GET_IDREG_WRITABLE 在该系列中似乎未被使用，并认为这是早期重构的遗留物，建议将其移除。Cornelia Huck 也同意这一观点，表示可以去掉该功能。整体来看，本周的讨论集中在补丁的细节优化和清理上。

#### 📝 邮件列表

1. **[04-14 18:38]** [PATCH v3 00/10] kvm/arm: Introduce a customizable aarch64 KVM host model
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[04-14 18:38]** [PATCH v3 05/10] arm/cpu: accessors for writable id registers
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[04-29 18:27]** Re: [PATCH v3 05/10] arm/cpu: accessors for writable id registers
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[04-30 15:48]** Re: [PATCH v3 05/10] arm/cpu: accessors for writable id registers
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 14: [PATCH] arm64: kvm: Replace ternary flags with str_on_off() helper

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 15 Apr 2025 10:24:05 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 KVM 的补丁，旨在用 `str_on_off()` 辅助函数替换重复的三元表达式，以提高代码可读性并确保跟踪点字符串格式的一致性。该补丁由 Seongsu Park 提出，并在历史讨论中得到了 Anshuman Khandual 的审核认可。

在之前的讨论中，Seongsu Park 提出了补丁的具体内容，并强调了其对代码可读性的改善。Anshuman Khandual 对该补丁表示支持，给予了“审核通过”的反馈。

在本周的新讨论中，Seongsu Park 再次询问 Anshuman 是否有任何反馈，并表示认为该补丁是合适的。Marc Zyngier 对补丁的看法是合理的，但指出由于该补丁主要是外观上的改动，因此不急于立即合并。他提到在准备 6.16 版本的补丁时，可能会将其纳入考虑。

总结来看，该补丁在技术上得到了支持，但由于其性质，合并进程将会稍作延迟。

#### 📝 邮件列表

1. **[04-15 10:24]** [PATCH] arm64: kvm: Replace ternary flags with str_on_off() helper
   - 发件人: Seongsu Park <sgsu.park@samsung.com>
2. **[04-15 12:06]** Re: [PATCH] arm64: kvm: Replace ternary flags with str_on_off()
 helper
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[04-28 16:11]** RE: [PATCH] arm64: kvm: Replace ternary flags with str_on_off()
 helper
   - 发件人: Seongsu Park <sgsu.park@samsung.com>
4. **[04-28 11:04]** Re: [PATCH] arm64: kvm: Replace ternary flags with str_on_off() helper
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 24 Apr 2025 19:47:41 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 AmpereOne 处理器的 erratum AC04_CPU_23 的补丁（PATCH v2），旨在通过在 HCR_EL2 寄存器的存储操作前后添加 DSB 和 ISB 指令，来防止数据地址的同时翻译被破坏。历史讨论中，D Scott Phillips 提出了补丁的具体实现细节，并解释了该问题的影响范围。

在之前的讨论中，参与者们关注到该补丁可能未能覆盖某些早期代码执行的情况，特别是在 C 代码执行之前的汇编代码（如 head.S 和 hyp-stub.S）可能也会受到影响。Marc Zyngier 提出，默认启用该补丁可能更为安全，只有在确认系统正常后再放宽限制。

本周的新讨论中，Marc Zyngier 强调了早期代码可能受到影响的风险，并建议在文档中记录这一点。D Scott Phillips 认可了这一观点，并表示将进一步检查所有相关代码，不仅限于 C 代码，以确保补丁的有效性和安全性。整体来看，讨论集中在如何全面评估和修正可能的漏洞，以确保系统的稳定性。

#### 📝 邮件列表

1. **[04-24 19:47]** [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
2. **[04-30 16:53]** Re: [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-01 08:17]** Re: [PATCH v2] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>

---

### Thread 16: [PATCH] KVM: selftests: add test for SVE host corruption

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 17 Apr 2025 00:32:49 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的自测试补丁，旨在添加一个测试程序以验证 SVE（Scalable Vector Extension）主机状态是否存在被丢弃的问题。该补丁由 Mark Brown 提交，基于 Mark Rutland 原始编写的程序进行轻微修改，主要用于检查在运行虚拟机时 SVE 寄存器状态是否出现损坏。

在历史讨论中，Mark Brown 提到，之前的内核版本在执行 KVM_RUN ioctl 后，若来宾未执行任何 FPSIMD/SVE/SME 指令，可能会意外丢弃 SVE 状态。此问题已在提交 fbc7e61195e2 中得到修复。补丁的目的是通过运行简单的虚拟机来验证这一修复。

在本周的新讨论中，Mark Rutland 对补丁提出了一些建议，指出当前测试并不能完全验证问题的缺失，因为可能会被抢占掩盖。他建议在测试中加入对 SVE 状态的操控，以更好地检测该问题。此外，他提到补丁中的一些 printf() 调用可能不再必要，并表示支持该补丁的继续推进。Mark Brown 随后确认了 Rutland 的建议，并表示将更新提交信息以恢复他的签名。

总体来看，本周讨论集中在补丁的细节修改和测试的有效性上，参与者对补丁的推进持积极态度。

#### 📝 邮件列表

1. **[04-17 00:32]** [PATCH] KVM: selftests: add test for SVE host corruption
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[04-29 16:27]** Re: [PATCH] KVM: selftests: add test for SVE host corruption
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[04-30 09:48]** Re: [PATCH] KVM: selftests: add test for SVE host corruption
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 17: [PATCH V2] arm64/mm: Implement pte_po_index() for permission overlay index

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 15 Apr 2025 11:14:42 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构下实现 `pte_po_index()` 函数，以支持权限覆盖索引。最初的补丁由 Ryan Roberts 提出，目的是解决 `pte_access_permitted()` 函数在处理 128 位数据时无法使用 `FIELD_GET()` 的问题。补丁建议创建一个专门的帮助函数 `pte_po_index()`，以便在不同数据类型宽度下进行必要的掩码和位移操作。

在历史讨论中，参与者们关注了如何有效地为即将添加的 D128 页表支持进行准备。补丁的背景是 Anshuman Khandual 在其私有分支中添加了 D128 页表支持，但尚未为 KVM 实现。

本周的新讨论中，Will Deacon 提出了对补丁的疑虑，认为目前的补丁和其他零散的补丁使得整体方向不明确，并建议可能需要对 KVM 页表代码进行相应的支持。Ryan Roberts 进一步澄清了补丁的背景，强调 D128 支持尚未准备好上游提交，并表示 Anshuman 的工作主要是为 D128 的实现做准备，目的是尽量减少代码差异。

总体来看，当前讨论集中在如何有效地推进 D128 页表支持的同时，确保与 KVM 的兼容性和清晰的开发方向。

#### 📝 邮件列表

1. **[04-15 11:14]** [PATCH V2] arm64/mm: Implement pte_po_index() for permission overlay index
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[04-29 16:11]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Will Deacon <will@kernel.org>
3. **[04-29 17:45]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>

---

### Thread 18: [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 15:47:10 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁，主题为“提供基本的 EL2 设置以支持在 EL0/1 中使用 FEAT_{LS64, LS64_V}”。该补丁旨在改善虚拟化环境下的处理能力，特别是在 KVM（内核虚拟机）客体中。

在之前的讨论中，参与者 Yicong Yang 提出了关于 HCRX 设置在 KVM 客体切换时的生存性问题。他指出，返回主机时会恢复 HCRX_HOST_FLAGS，这可能导致 GCS 代码出现问题，暗示补丁可能存在缺陷。

本周的讨论中，Will Deacon 对 Yicong Yang 的担忧进行了回应，强调了 HCRX 设置在世界切换中的处理方式，并表示可能存在问题。此外，他对补丁中的标签命名表示认可，认为目前的命名是合理的。

总体来看，本周的讨论主要集中在补丁的潜在问题及其命名的合理性上，尚未达成明确的结论。

#### 📝 邮件列表

1. **[04-29 15:47]** Re: [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1
   - 发件人: Will Deacon <will@kernel.org>
2. **[04-29 15:47]** Re: [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 19: [PATCH v2 0/7] Move pKVM ownership state to hyp_vmemmap

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 16 Apr 2025 15:26:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是将 pKVM 的所有权状态迁移到 hyp_vmemmap。历史讨论中，Quentin Perret 提出了这一系列补丁的主要目的，包括降低超管状态查找的成本，避免进行 hyp 阶段的页面表遍历，以及将 hyp 状态与线性映射的存在解耦，以便于未来功能的扩展和现有代码的清理。

在本周的新讨论中，Marc Zyngier 确认已将补丁应用到下一个版本中，并列出了七个相关补丁的提交信息。这些补丁包括对 SVE 状态的跟踪、修复 pKVM 页面跟踪的注释、引入帮助函数、将 hyp 状态迁移到 hyp_vmemmap 等。整体来看，本周的进展表明该系列补丁得到了认可并已进入开发流程。

#### 📝 邮件列表

1. **[04-16 15:26]** [PATCH v2 0/7] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
2. **[04-29 14:41]** Re: [PATCH v2 0/7] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH for-10.1 v5 00/13] arm: rework id register storage

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 18:43:50 +0200

#### 🤖 AI 总结

本邮件线程讨论的是一个针对 ARM 架构的补丁，主题为“重新设计 ID 寄存器存储”（[PATCH for-10.1 v5 00/13] arm: rework id register storage）。该补丁旨在优化 ARM 系统中 ID 寄存器的存储方式。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁经过了初步的审查和讨论，可能涉及到寄存器存储的效率和准确性问题。

在本周的新讨论中，参与者 Eric Auger 和 Cornelia Huck 进行了进一步的交流。Eric 提到他在审查过程中发现了一些转换错误，并表示在修正这些错误后，补丁应该可以通过审查。Cornelia 则回应称她已对这些问题进行了修正，并在最后几个案例中将 `fdarray[2]` 修改为 `fd`。她表示在进行一些测试后，可能会重新提交补丁。

总体来看，本周的讨论集中在对补丁的细节审查和错误修正上，显示出参与者之间的协作和对代码质量的关注。

#### 📝 邮件列表

1. **[04-28 18:43]** Re: [PATCH for-10.1 v5 00/13] arm: rework id register storage
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 12:05]** Re: [PATCH for-10.1 v5 00/13] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 21: [PATCH for-10.1 v5 08/13] arm/cpu: Store id_isar0-7 into the
 idregs array

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 18:04:36 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM CPU 的补丁，旨在将 id_isar0-7 存储到 idregs 数组中。补丁的编号为 [PATCH for-10.1 v5 08/13]，目前尚未提供详细的补丁内容。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了改进 ARM CPU 的寄存器管理，可能涉及到对现有代码的优化或修复。

在本周的新讨论中，Eric Auger 对补丁提出了批评，指出其中存在问题，特别是关于 SET_IDREG 的使用不当，建议应使用 SET_IDREG(isar, ID_ISAR5, 0x0) 的方式进行修正。Cornelia Huck 随后回应表示对问题的来源感到困惑，并承诺会进行修复。这表明补丁在实现上存在一定的错误，需要进一步的修改和验证。

总体来看，本周的讨论集中在补丁的具体实现问题上，参与者们正在积极寻求解决方案。

#### 📝 邮件列表

1. **[04-28 18:04]** Re: [PATCH for-10.1 v5 08/13] arm/cpu: Store id_isar0-7 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:51]** Re: [PATCH for-10.1 v5 08/13] arm/cpu: Store id_isar0-7 into the
 idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 22: [PATCH for-10.1 v5 06/13] arm/cpu: Store aa64dfr0/1 into the
 idregs array

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 17:56:28 +0200

#### 🤖 AI 总结

本邮件讨论的主题是一个针对 ARM CPU 的补丁，内容为将 aa64dfr0 和 aa64dfr1 寄存器的值存储到 idregs 数组中。该补丁旨在增强 ARM 架构的寄存器管理，确保相关信息的正确存储和访问。

在之前的讨论中，参与者们并未提供具体的背景信息或详细的技术讨论，因此我们无法获取更多历史讨论的要点。

在本周的新讨论中，Eric Auger 指出补丁中的一行代码重复，Cornelia Huck 随后确认了这一问题，并表示将进行修复。这表明补丁在提交前需要进一步的审查和修改，以确保代码的质量和准确性。整体来看，本周的讨论主要集中在对补丁代码的细节修正上。

#### 📝 邮件列表

1. **[04-28 17:56]** Re: [PATCH for-10.1 v5 06/13] arm/cpu: Store aa64dfr0/1 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:48]** Re: [PATCH for-10.1 v5 06/13] arm/cpu: Store aa64dfr0/1 into the
 idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 23: [PATCH for-10.1 v5 04/13] arm/cpu: Store aa64pfr0/1 into the
 idregs array

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 17:39:28 +0200

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH for-10.1 v5 04/13] arm/cpu: Store aa64pfr0/1 into the idregs array”的补丁旨在将 ARM 架构中的 aa64pfr0 和 aa64pfr1 寄存器值存储到 idregs 数组中，以便更好地管理和访问这些寄存器信息。

在之前的讨论中，参与者 Cornelia Huck 和 Eric Auger 指出补丁中存在一个转换错误，具体是关于 ID_PFR0_EL1 和 ID_PFR1_EL1 的定义。Eric Auger 提到在补丁中定义的寄存器可能不正确，导致了对寄存器的误用。

在本周的新讨论中，Eric Auger 确认了之前的错误，并表示将对此进行修正。Cornelia Huck 也支持这一观点，确认了错误的寄存器定义需要更正。整体来看，本周的讨论集中在修复补丁中的错误上，确保补丁能够正确实现其预期功能。

#### 📝 邮件列表

1. **[04-28 17:39]** Re: [PATCH for-10.1 v5 04/13] arm/cpu: Store aa64pfr0/1 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:38]** Re: [PATCH for-10.1 v5 04/13] arm/cpu: Store aa64pfr0/1 into the
 idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 24: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0 into
 the idregs arrays

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 16:52:02 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM 架构的补丁（PATCH），具体内容为将 `aa64isar0` 和 `aa64zfr0` 存储到 ID 寄存器数组中。该补丁的目的是改进 ARM CPU 的寄存器管理，以提高虚拟化性能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是基于对现有寄存器处理方式的改进需求。参与者们可能之前讨论了补丁的必要性和实现细节。

在本周的新讨论中，Eric Auger 和 Cornelia Huck 进行了简短的交流。Eric 提到可以在补丁中添加 KVM（Kernel-based Virtual Machine）相关的功能，并建议在其他调用中使用文件描述符（fd）而不是 `fdarray[2]`，但这可以在后续版本中处理。Cornelia 则表示，既然该系列补丁需要重新整理（respin），那么可以顺便进行这些改动。

总体来看，本周的讨论主要集中在补丁的细节优化和后续版本的计划上，显示出参与者对改进补丁质量的重视。

#### 📝 邮件列表

1. **[04-28 16:52]** Re: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0 into
 the idregs arrays
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:31]** Re: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0
 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 25: [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  1 May 2025 16:24:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `host_stage2_set_owner_locked()` 函数中的内存检查错误。

**原始补丁内容**：
补丁由 Mostafa Saleh 提交，主要修复了在 `host_stage2_set_owner_locked()` 函数中对内存地址的检查逻辑。原代码使用 `addr_is_memory(addr)` 来判断地址是否为有效内存，但该检查不够准确。补丁将其修改为 `range_is_memory(addr, addr + size)`，以确保检查的范围涵盖了整个内存区域，避免潜在的内核崩溃。

**之前的讨论要点**：
本邮件线程没有历史讨论，所有内容均为本周的新讨论。

**本周的新讨论与进展**：
Mostafa Saleh 提出了该补丁，并指出这是在为 pKVM 准备其他补丁时发现的一个简单错误。他认为这个错误在正常情况下是无害的，但如果处理不当可能导致内核崩溃。补丁已经提交，并包含了对相关代码的具体修改。此补丁的签名也由作者附上，显示出其正式性和可信度。

#### 📝 邮件列表

1. **[05-01 16:24]** [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 26: [PATCH] arm64: Expose AIDR_EL1 via sysfs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 21:27:51 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 arm64 架构的补丁，旨在通过 sysfs 暴露 AIDR_EL1 寄存器。补丁的具体内容是将 AIDR_EL1 的信息通过系统文件系统提供给用户空间，以便于用户进行访问和监控。

在历史讨论中，并没有提供具体的背景信息或之前的讨论内容，因此我们无法得知该补丁的起源或相关的技术细节。

在本周的新讨论中，参与者 Will Deacon 确认该补丁已经被应用到 arm64 的开发分支（for-next/cpufeature），并感谢了补丁的提交者 Oliver Upton。这表明该补丁已获得认可，并将继续在未来的开发中使用。

总结而言，本周的讨论主要集中在补丁的应用确认上，未涉及其他争议或深入讨论。

#### 📝 邮件列表

1. **[04-29 21:27]** Re: [PATCH] arm64: Expose AIDR_EL1 via sysfs
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 27: [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 12:43:26 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 在 arm64 架构下的一个补丁，目的是在 VHE 模式下强制将 HCR_EL2.xMO 设为 1。补丁的提出者是 Marc Zyngier，补丁编号为 [PATCH v2]。

在历史讨论中没有相关内容，补丁的背景是当前在 VHE 模式下，HCR_EL2.xMO 位的设置和清除是多余的，因为物理中断始终需要传递给宿主机。补丁指出，清除这些位会导致两个主要问题：一是当这些位被清除时，IRQ 无法被处理；二是在 AmpereOne 硬件上清除这些位会引发严重的错误（AC03_CPU_36）。

本周的新讨论中，Marc Zyngier 详细阐述了补丁的必要性，并表示将通过永久设置 xMO 位来解决上述问题。这一改动需要对依赖于动态切换这些位的代码路径进行一些调整，但在初始化阶段的设置将保持不变，以确保在中断禁用的情况下安全运行。

总的来说，本周的讨论集中在补丁的具体实现及其对系统稳定性的影响上，强调了在 VHE 模式下强制设置 HCR_EL2.xMO 位的重要性。

#### 📝 邮件列表

1. **[04-29 12:43]** [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 28: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 11:07:28 +0530

#### 🤖 AI 总结

本邮件主题为“[PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9”，主要讨论了针对 ARM64 架构的一个补丁。该补丁的目的是启用 EL2（异常级别 2）对 FEAT_PMUv3p9 特性的要求。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是为了支持 ARM64 架构中性能监控单元（PMU）新特性的实现，确保在引导过程中满足 EL2 的相关要求。

在本周的新讨论中，参与者 Anshuman Khandual 提到该补丁及其所需的工具 sysreg 补丁已经合并到适用的稳定分支中，并在版本 v6.12.25 和 v6.14.4 中可用。这表明补丁的开发和集成工作已经完成，并且相关功能已正式上线，为 ARM64 的性能监控提供了支持。

#### 📝 邮件列表

1. **[04-29 11:07]** Re: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 29: [PATCH for-10.1 v5 13/13] arm/cpu: switch to a generated
 cpu-sysregs.h.inc

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 28 Apr 2025 18:38:04 +0200

#### 🤖 AI 总结

本邮件主题为“[PATCH for-10.1 v5 13/13] arm/cpu: switch to a generated cpu-sysregs.h.inc”，主要讨论了针对 ARM 架构 CPU 的一个补丁。该补丁的目的是将 CPU 系统寄存器的定义切换到一个生成的头文件 `cpu-sysregs.h.inc` 中，以提高代码的可维护性和可读性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了优化 ARM CPU 的系统寄存器管理，可能涉及到之前的代码结构或实现方式的问题。

在本周的新讨论中，参与者 Eric Auger 对该补丁进行了审核，并表示支持，标记为“Reviewed-by”。这表明补丁得到了认可，可能会在后续版本中被合并。

总体来看，本周的讨论主要集中在对补丁的审核和认可上，表明该补丁在开发过程中得到了积极的反馈，预计将推动 ARM CPU 系统寄存器管理的改进。

#### 📝 邮件列表

1. **[04-28 18:38]** Re: [PATCH for-10.1 v5 13/13] arm/cpu: switch to a generated
 cpu-sysregs.h.inc
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 30: [PATCH for-10.1 v5 03/13] arm/cpu: Store aa64isar1/2 into the
 idregs array

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 28 Apr 2025 17:00:41 +0200

#### 🤖 AI 总结

本邮件讨论的主题是一个针对 ARM CPU 的补丁，内容为将 aa64isar1 和 aa64isar2 存储到 idregs 数组中。该补丁的目的是优化 ARM 架构下的 CPU 信息存储方式。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是基于对 ARM CPU 信息管理的改进需求。补丁的实现可能涉及到对现有数据结构的调整，以提高数据访问效率。

在本周的新讨论中，参与者 Eric Auger 对补丁进行了审阅，并提出了一个小的改进建议，建议在后续的简化补丁中将 `fdarray[2]` 替换为 `fd`，以提高代码的可读性。Eric 认为补丁在经过进一步审阅后整体上是良好的，显示出对补丁的认可。

总结来看，该补丁旨在改善 ARM CPU 的信息存储方式，虽然历史讨论不详，但本周的反馈表明补丁在审查过程中得到了积极的评价，并有潜在的简化方向。

#### 📝 邮件列表

1. **[04-28 17:00]** Re: [PATCH for-10.1 v5 03/13] arm/cpu: Store aa64isar1/2 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 13:40:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在解决 MTE（Memory Tagging Extension）相关的支持问题。

1. **原始补丁内容**：Ben Horgan 提出的补丁系列（RFC PATCH 0/3）主要关注 ID_AA64PFR1_EL1.MTE_frac 字段的处理。当前情况下，KVM 隐藏了该字段，导致在某些主机上，即使不支持 MTE_ASYNC，客人系统仍会错误地看到该功能被声明为支持。补丁旨在修复这一问题，确保只有在实际支持的情况下，才向客人系统报告 MTE_ASYNC。

2. **之前讨论要点**：在历史讨论中，Marc Zyngier 提出对补丁的改进建议，强调应限制对硬件支持的传播，以避免未来可能的兼容性问题。他指出，MTE_frac 的处理应更为谨慎，特别是在 MTE3 的情况下。

3. **本周的新讨论与进展**：在本周的讨论中，Ben Horgan 对 Marc 的建议表示认可，并提出了更新条件的方案，以确保在 MTE2 支持的情况下，MTE_frac 的处理更为安全。他计划修改代码逻辑，以更准确地反映硬件能力。

总体来看，讨论围绕如何正确处理 MTE_frac 字段展开，确保 KVM 在不同硬件支持情况下的准确性和稳定性。

#### 📝 邮件列表

1. **[04-14 13:40]** [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[04-14 13:40]** [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[04-27 18:24]** Re: [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-28 12:26]** Re: [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on
 MTE capability
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

