# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 09:02:52

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 199
- **总 Thread 数**: 30
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 12 threads (135 邮件)
- **RFC**: 3 threads (48 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Other**: 14 threads (14 邮件)

---

## 📌 PATCH

共 12 个 thread

---

### Thread 1: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling

**📧 邮件数**: 43 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 26 Apr 2025 13:27:54 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM (Kernel-based Virtual Machine) 在 ARM64 架构下的细粒度陷阱处理的补丁系列，主要集中在对 FEAT_FGT2（细粒度陷阱2）功能的重构和实现。

1. **原始补丁/问题内容**：
   - 该补丁系列的目标是改进 ARM64 架构下 KVM 的细粒度陷阱处理，特别是引入对 FEAT_FGT2 的支持。补丁的数量为 42 个，涵盖了对相关寄存器的添加、描述和处理逻辑的改进。

2. **之前讨论要点**：
   - 在之前的讨论中，Marc Zyngier 提到该系列补丁的规模显著增加，主要是因为添加了对 FEAT_FGT2 的全面支持。补丁中还包括对现有代码的重构，以减少冗余和提高可读性。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，补丁系列得到了进一步的细化，包括对 FEAT_FGT2 寄存器的描述、陷阱路由的实现、以及对寄存器的上下文切换支持。此外，Marc Zyngier 提到需要使用 KVM 自身的 FGT 表来构建寄存器的视图，并确保在初始化时验证 FGT 描述与 RES0 掩码的一致性。补丁还引入了对 HCRX_EL2 寄存器的特征映射，以便更好地管理其 RES0 状态。整体上，这些改进旨在增强 KVM 在 ARM64 上的功能和稳定性。

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
6. **[04-26 13:27]** [PATCH v3 05/42] arm64: sysreg: Update ID_AA64PFR0_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-26 13:28]** [PATCH v3 06/42] arm64: sysreg: Update PMSIDR_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-26 13:28]** [PATCH v3 07/42] arm64: sysreg: Update TRBIDR_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-26 13:28]** [PATCH v3 08/42] arm64: sysreg: Add registers trapped by HFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-26 13:28]** [PATCH v3 09/42] arm64: sysreg: Add registers trapped by HDFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-26 13:28]** [PATCH v3 10/42] arm64: sysreg: Add system instructions trapped by HFGIRT2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-26 13:28]** [PATCH v3 11/42] arm64: Remove duplicated sysreg encodings
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-26 13:28]** [PATCH v3 12/42] arm64: tools: Resync sysreg.h
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-26 13:28]** [PATCH v3 13/42] arm64: Add syndrome information for trapped LD64B/ST64B{,V,V0}
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[04-26 13:28]** [PATCH v3 14/42] arm64: Add FEAT_FGT2 capability
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[04-26 13:28]** [PATCH v3 15/42] KVM: arm64: Tighten handling of unknown FGT groups
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[04-26 13:28]** [PATCH v3 16/42] KVM: arm64: Simplify handling of negative FGT bits
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[04-26 13:28]** [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[04-26 13:28]** [PATCH v3 18/42] KVM: arm64: Restrict ACCDATA_EL1 undef to FEAT_ST64_ACCDATA being disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[04-26 13:28]** [PATCH v3 19/42] KVM: arm64: Don't treat HCRX_EL2 as a FGT register
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[04-26 13:28]** [PATCH v3 20/42] KVM: arm64: Plug FEAT_GCS handling
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[04-26 13:28]** [PATCH v3 21/42] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[04-26 13:28]** [PATCH v3 22/42] KVM: arm64: Add description of FGT bits leading to EC!=0x18
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[04-26 13:28]** [PATCH v3 23/42] KVM: arm64: Use computed masks as sanitisers for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[04-26 13:28]** [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[04-26 13:28]** [PATCH v3 25/42] KVM: arm64: Propagate FGT masks to the nVHE hypervisor
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[04-26 13:28]** [PATCH v3 26/42] KVM: arm64: Use computed FGT masks to setup FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[04-26 13:28]** [PATCH v3 27/42] KVM: arm64: Remove hand-crafted masks for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[04-26 13:28]** [PATCH v3 28/42] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[04-26 13:28]** [PATCH v3 29/42] KVM: arm64: Handle PSB CSYNC traps
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[04-26 13:28]** [PATCH v3 30/42] KVM: arm64: Switch to table-driven FGU configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[04-26 13:28]** [PATCH v3 31/42] KVM: arm64: Validate FGT register descriptions against RES0 masks
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[04-26 13:28]** [PATCH v3 32/42] KVM: arm64: Use FGT feature maps to drive RES0 bits
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[04-26 13:28]** [PATCH v3 33/42] KVM: arm64: Allow kvm_has_feat() to take variable arguments
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[04-26 13:28]** [PATCH v3 34/42] KVM: arm64: Use HCRX_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[04-26 13:28]** [PATCH v3 35/42] KVM: arm64: Use HCR_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[04-26 13:28]** [PATCH v3 36/42] KVM: arm64: Add FEAT_FGT2 registers to the VNCR page
   - 发件人: Marc Zyngier <maz@kernel.org>
38. **[04-26 13:28]** [PATCH v3 37/42] KVM: arm64: Add sanitisation for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
39. **[04-26 13:28]** [PATCH v3 38/42] KVM: arm64: Add trap routing for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
40. **[04-26 13:28]** [PATCH v3 39/42] KVM: arm64: Add context-switch for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
41. **[04-26 13:28]** [PATCH v3 40/42] KVM: arm64: Allow sysreg ranges for FGT descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[04-26 13:28]** [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Marc Zyngier <maz@kernel.org>
43. **[04-26 13:28]** [PATCH v3 42/42] KVM: arm64: Handle TSB CSYNC traps
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v3 0/6] Add FIELD_MODIFY() helper

**📧 邮件数**: 29 | **👥 参与者**: 8 | **📅 开始时间**: Thu, 17 Apr 2025 18:47:07 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是引入一个新的宏 `FIELD_MODIFY()`，旨在增强 Linux 内核中位域操作的安全性和可读性。该宏与现有的 `xxx_replace_bits()` 函数相似，但提供了编译时类型检查，能够捕捉不正确的参数类型错误。

在历史讨论中，Luo Jie 提出了这一补丁系列，并解释了 `FIELD_MODIFY()` 的功能和优势。尽管有参与者对引入新宏表示怀疑，认为现有的 `_replace_bits()` 函数已经足够，但其他人则指出，现有函数缺乏文档支持，且错误检查仅在运行时进行，可能导致潜在的溢出错误。

在本周的新讨论中，参与者们对 `FIELD_MODIFY()` 的使用进行了积极的反馈。Markus Elfring 提出了对补丁的具体修改建议，并讨论了支持其他操作模式的可能性。Jie Luo 确认将根据反馈更新补丁，并表示该宏将在 Qualcomm 的以太网驱动中得到应用。此外，Yury Norov 和 Russell King 之间关于使用 `FIELD_MODIFY()` 和 `_replace_bits()` 的技术细节进行了深入讨论，强调了编译器在捕捉错误方面的优势。

总体而言，`FIELD_MODIFY()` 的引入得到了逐步认可，参与者们认为其在提高代码可读性和安全性方面具有重要意义。

#### 📝 邮件列表

1. **[04-17 18:47]** [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[04-17 18:47]** [PATCH v3 1/6] bitfield: Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
3. **[04-17 18:47]** [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
4. **[04-17 18:47]** [PATCH v3 3/6] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
5. **[04-17 18:47]** [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
6. **[04-17 12:10]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-17 12:23]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-17 19:22]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Andrew Lunn <andrew@lunn.ch>
9. **[04-17 18:45]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-17 19:11]** Re: [PATCH v3 3/6] arm64: tlb: Convert the opencoded field modify
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
11. **[04-18 11:08]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
12. **[04-18 11:14]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Yury Norov <yury.norov@gmail.com>
13. **[04-18 16:35]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-18 13:04]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
15. **[04-18 13:11]** Re: [PATCH v3 1/6] bitfield: Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
16. **[04-23 13:01]** Re: [cocci] [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
17. **[04-23 21:04]** Re: [cocci] [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
18. **[04-23 21:05]** Re: [PATCH v3 1/6] bitfield: Add FIELD_MODIFY() helper
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
19. **[04-23 21:15]** Re: [PATCH v3 3/6] arm64: tlb: Convert the opencoded field modify
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
20. **[04-23 21:19]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Jie Luo <quic_luoj@quicinc.com>
21. **[04-23 18:35]** Re: [cocci] [PATCH v3 2/6] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
22. **[04-23 16:54]** RE: [cocci] [PATCH v3 3/6] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Keller, Jacob E <jacob.e.keller@intel.com>
23. **[04-23 18:44]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
24. **[04-23 18:48]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
25. **[04-23 14:27]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Yury Norov <yury.norov@gmail.com>
26. **[04-23 14:44]** Re: [PATCH v3 0/6] Add FIELD_MODIFY() helper
   - 发件人: Yury Norov <yury.norov@gmail.com>
27. **[04-23 20:11]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Russell King (Oracle) <linux@armlinux.org.uk>
28. **[04-23 15:40]** Re: [PATCH v3 4/6] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Yury Norov <yury.norov@gmail.com>
29. **[04-24 15:24]** RE: [cocci] [PATCH v3 3/6] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Keller, Jacob E <jacob.e.keller@intel.com>

---

### Thread 3: [PATCH v3 00/17] KVM: arm64: Recursive NV support

**📧 邮件数**: 18 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 23 Apr 2025 16:14:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现递归虚拟化（Recursive NV）支持的补丁系列（PATCH v3 00/17）。该系列补丁的核心在于实现 VNCR（Virtual Non-volatile Control Register）支持，特别是 VNCR_EL2 的虚拟化。

**原始补丁/问题的内容**：
补丁的目标是实现对 VNCR_EL2 的支持，允许在嵌套虚拟化环境中正确处理系统寄存器的访问。补丁中提到，VNCR_EL2 的地址是虚拟地址，必须在 EL2 上进行映射，以便 L2 虚拟机能够访问。

**之前讨论的要点**：
在历史讨论中，Marc Zyngier 提到，虚拟化 VNCR 的过程涉及到复杂的上下文切换和内存管理，尤其是 TLB（Translation Lookaside Buffer）的管理。补丁系列的实现旨在确保在正确的时间拥有正确的页面，并处理可能导致页面不可访问的各种情况。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在补丁的具体实现上，包括：
1. **VNCR_EL2 的布局添加**，确保系统能够正确识别和处理 VNCR_EL2。
2. **动态分配 VNCR 页面**，以支持系统寄存器访问。
3. **处理 VNCR_EL2 触发的故障**，确保在发生故障时能够正确映射和处理。
4. **实现 TLB 无效化机制**，以支持跨 CPU 的 TLB 操作。
5. **允许用户空间请求 KVM_ARM_VCPU_EL2 功能**，使得用户能够启用嵌套虚拟化。

总体而言，该系列补丁的实现使得 KVM 在 arm64 架构上对递归虚拟化的支持更加完善，尽管仍存在一些未解决的细节问题。

#### 📝 邮件列表

1. **[04-23 16:14]** [PATCH v3 00/17] KVM: arm64: Recursive NV support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-23 16:14]** [PATCH v3 01/17] arm64: sysreg: Add layout for VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-23 16:14]** [PATCH v3 02/17] KVM: arm64: nv: Allocate VNCR page when required
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-23 16:14]** [PATCH v3 03/17] KVM: arm64: nv: Extract translation helper from the AT code
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-23 16:14]** [PATCH v3 04/17] KVM: arm64: nv: Snapshot S1 ASID tagging information during walk
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-23 16:14]** [PATCH v3 05/17] KVM: arm64: nv: Move TLBI range decoding to a helper
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-23 16:14]** [PATCH v3 06/17] KVM: arm64: nv: Don't adjust PSTATE.M when L2 is nesting
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-23 16:14]** [PATCH v3 07/17] KVM: arm64: nv: Add pseudo-TLB backing VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-23 16:14]** [PATCH v3 08/17] KVM: arm64: nv: Add userspace and guest handling of VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-23 16:15]** [PATCH v3 09/17] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-23 16:15]** [PATCH v3 10/17] KVM: arm64: nv: Handle mapping of VNCR_EL2 at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-23 16:15]** [PATCH v3 11/17] KVM: arm64: nv: Handle VNCR_EL2 invalidation from MMU notifiers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-23 16:15]** [PATCH v3 12/17] KVM: arm64: nv: Program host's VNCR_EL2 to the fixmap address
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-23 16:15]** [PATCH v3 13/17] KVM: arm64: nv: Add S1 TLB invalidation primitive for VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[04-23 16:15]** [PATCH v3 14/17] KVM: arm64: nv: Plumb TLBI S1E2 into system instruction dispatch
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[04-23 16:15]** [PATCH v3 15/17] KVM: arm64: nv: Remove dead code from ERET handling
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[04-23 16:15]** [PATCH v3 16/17] KVM: arm64: Allow userspace to request KVM_ARM_VCPU_EL2*
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[04-23 16:15]** [PATCH v3 17/17] KVM: arm64: Document NV caps and vcpu flags
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags

**📧 邮件数**: 16 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 7 Apr 2025 08:20:09 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在允许使用 VMA（虚拟内存区域）标志创建可缓存的二级映射。补丁的核心是解决在处理 PFNMAP（页框号映射）时的缓存属性问题。

在历史讨论中，参与者们探讨了 KVM 如何处理 VMA 中的 PTE（页表项）复制，特别是在物理地址缺少结构页的情况下，KVM 如何假设最坏情况并处理缓存刷新。讨论中提到，KVM 需要一个能力标志来指示内核是否支持可缓存的 PFNMAP 映射，但有些参与者认为这并不必要，因为用户空间的选择有限。

在本周的新讨论中，Ankit Agrawal 提醒大家确认是否需要“可缓存 PFNMAP”能力标志。Oliver Upton 强调用户空间需要了解内存属性，以便在进行虚拟机迁移时保持一致性。Jason Gunthorpe 则质疑是否有必要增加内存插槽标志，认为这会增加复杂性。Sean Christopherson 强烈反对添加内存插槽标志，认为仅依靠每个虚拟机的能力标志就足够了。整体来看，讨论围绕如何在 KVM 中有效管理缓存属性和用户空间的参与展开，尚未达成一致。

#### 📝 邮件列表

1. **[04-07 08:20]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[04-07 13:15]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
3. **[04-07 09:43]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[04-16 08:51]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
5. **[04-21 16:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
6. **[04-22 00:49]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[04-22 10:54]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
8. **[04-22 07:53]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[04-22 17:50]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[04-22 14:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
11. **[04-22 14:28]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[04-22 20:35]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
13. **[04-23 11:45]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
14. **[04-23 09:02]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
15. **[04-23 13:26]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
16. **[04-23 10:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>

---

### Thread 5: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 16 Apr 2025 14:41:22 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 的 KVM 支持的补丁系列（PATCH v8 00/43）。该补丁旨在实现受保护虚拟机的运行，相关的客体支持已在 v6.14-rc1 版本中合并。

在历史讨论中，补丁的主要内容包括增加了对 KVM 的支持，文档更新以及对 SMC 调用 RMM（Realm Management Monitor）的定义和包装函数的添加。这些补丁经过多次修改，主要集中在增强文档、重命名参数和改善代码注释等方面。

在本周的新讨论中，参与者 Suzuki K Poulose 对补丁进行了审查，并提出了一些小的修改建议。他确认了补丁中关于 HIPAS 和 RMI_ASSIGNED 的描述，并对代码中的某些注释进行了澄清。此外，他还质疑了在 KVM 初始化时检查 RME 支持的必要性，认为如果主机在虚拟化环境下运行，可能会将调用转发给 RMM，这一问题并不紧急。

总体来看，本周的讨论主要集中在补丁的审查和细节调整上，未出现重大争议或新问题。

#### 📝 邮件列表

1. **[04-16 14:41]** [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[04-16 14:41]** [PATCH v8 03/43] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
3. **[04-16 14:41]** [PATCH v8 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
4. **[04-16 14:41]** [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
5. **[04-25 11:30]** Re: [PATCH v8 03/43] arm64: RME: Add SMC definitions for calling the
 RMM
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[04-25 11:48]** Re: [PATCH v8 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[04-25 11:53]** Re: [PATCH v8 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[04-25 12:08]** Re: [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 6: [PATCH 0/3] KVM: arm64: Address Translation fixes

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 22 Apr 2025 13:26:09 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的地址转换修复的补丁（PATCH 0/3）。该补丁系列旨在解决多个与地址转换相关的问题，包括错误报告、访问故障处理以及不当数据传递等。

在历史讨论中，补丁的背景主要集中在 KVM 的地址转换实现上，Marc Zyngier 提出了几个关键问题，例如在某些情况下错误报告 PAR_EL1.PTW，以及对访问故障的处理缺失，这可能导致系统崩溃。

在本周的新讨论中，Marc Zyngier 提交了三个具体的补丁：
1. **修复 PAR_EL1.PTW 和 S 的报告**：确保在地址转换失败时，正确报告 S2 的状态。
2. **处理访问故障**：更新 S1 转换代码以识别访问故障，确保系统能够正确响应这些情况。
3. **避免向 HCR_EL2 传递未初始化的数据**：简化 HCR_EL2 的保存和恢复过程，确保在执行 AT S1E{0,1} 时不引入错误数据。

此外，参与者 Joey Gouly 对第二个补丁进行了审核，而 D Scott Phillips 提出了关于 TCR_ELx.HA 的依赖性问题，Marc Zyngier 也对此进行了回应，指出当前支持的配置。

整体来看，本周的讨论集中在补丁的具体实现及其对系统稳定性的影响上，参与者们积极提出建议和反馈。

#### 📝 邮件列表

1. **[04-22 13:26]** [PATCH 0/3] KVM: arm64: Address Translation fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-22 13:26]** [PATCH 1/3] KVM: arm64: Fix PAR_EL1.{PTW,S} reporting on AT S1E*
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-22 13:26]** [PATCH 2/3] KVM: arm64: Teach address translation about access faults
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-22 13:26]** [PATCH 3/3] KVM: arm64: Don't feed uninitialised data to HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-22 14:50]** Re: [PATCH 2/3] KVM: arm64: Teach address translation about access
 faults
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[04-22 13:54]** Re: [PATCH 2/3] KVM: arm64: Teach address translation about access
 faults
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
7. **[04-22 22:19]** Re: [PATCH 2/3] KVM: arm64: Teach address translation about access faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 15 Apr 2025 08:47:10 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对AmpereOne处理器的错误修复补丁，具体是关于erratum AC03_CPU_36的问题。该错误可能导致异步异常在处理器控制寄存器HCR_EL2更新时被错误路由到异常级别。为了解决这个问题，补丁建议在受影响的机器上始终在阻止异步异常的情况下写入HCR_EL2。

在历史讨论中，D Scott Phillips提出了该补丁，并详细描述了错误的具体情况。Marc Zyngier对此进行了回应，确认了补丁的必要性，并讨论了处理器在不同模式下的行为。

在本周的新讨论中，D Scott Phillips提出了一个新观点，认为在nvhe模式下，由于异步异常始终被屏蔽，因此该错误不会发生。他询问Marc Zyngier对此的看法。Marc Zyngier同意这一观点，并指出nVHE/hVHE超管代码在处理HVC异常时会禁用中断，因此该情况是安全的。同时，他提到在处理SError时的代码路径可能存在问题，但认为在特定条件下该错误不会被触发。最终，他表示将继续推进补丁的修订版本。

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

---

### Thread 8: [PATCH 0/4] KVM: arm64: UBSAN at EL2

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 16 Apr 2025 18:04:30 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 架构中支持 UBSAN（Undefined Behavior Sanitizer）在 EL2 模式下的实现，相关的补丁集包含四个部分。

在历史讨论中，Mostafa Saleh 提出了补丁集，旨在为 EL2 模式添加 UBSAN 支持。补丁中提到，许多内核支持的 sanitizers 在 EL2 模式下被禁用，而 UBSAN 可以在两种模式下运行。补丁 3/4 引入了新的 Kconfig 选项 CONFIG_UBSAN_KVM_EL2，使得在受保护的 nvhe/hvhe 模式下可以启用 UBSAN。该补丁的主要变化是，EL2 模式下的错误处理将始终触发 "brk"，而不是实现钩子，因为虚拟机监控器无法打印报告。

在本周的新讨论中，Mostafa Saleh 回复了 Kees Cook 的建议，表示将会在补丁的 v2 版本中修正之前提到的格式和命名问题。整体来看，讨论进展顺利，补丁的细节正在逐步完善。

#### 📝 邮件列表

1. **[04-16 18:04]** [PATCH 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[04-16 18:04]** [PATCH 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[04-16 12:54]** Re: [PATCH 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Kees Cook <kees@kernel.org>
4. **[04-25 17:30]** Re: [PATCH 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 9: [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 22 Apr 2025 13:39:01 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 在 arm64 架构下的一个补丁，目的是在 VHE 模式下强制将 HCR_EL2.xMO 设置为 1。Marc Zyngier 提出，这样做是为了确保物理中断能够顺利到达主机，同时解决两个主要问题：一是避免在某些情况下中断无法被处理，二是防止在处理过程中清除这些位导致的硬件错误（AC03_CPU_36）。

在历史讨论中，虽然没有具体的邮件记录，但可以推测之前可能有关于如何处理 HCR_EL2.xMO 的讨论。Marc Zyngier 在补丁中指出，当前的做法是根据主机内核的角色不断设置和清除这些位，但实际上在 VHE 模式下始终希望中断能够到达主机，因此这种做法显得多余。

在本周的新讨论中，D Scott Phillips 提出是否应该在 `__vgic_v3_get_gic_config()` 函数中也去掉对 xMO 的处理。Marc Zyngier 认可了这一点，并表示会对该部分进行修改，计划发布补丁的第二版（v2）。整体来看，本周的讨论集中在补丁的细节调整和进一步优化上。

#### 📝 邮件列表

1. **[04-22 13:39]** [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-24 15:24]** Re: [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE
 mode
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
3. **[04-26 19:13]** Re: [PATCH] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 24 Apr 2025 19:47:41 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 AmpereOne 处理器的错误 AC04_CPU_23 的补丁（PATCH v2）。该补丁旨在解决在更新 HCR_EL2 时可能导致的数据地址翻译损坏问题。具体来说，补丁通过在对 HCR_EL2 进行存储之前添加数据同步屏障（DSB）和在之后添加指令同步屏障（ISB）来防止旧指令和新指令在执行过程中发生冲突，从而避免翻译错误。

在历史讨论中，补丁的初步版本（v1）已经提交，并在本周的新讨论中进行了更新。更新内容包括添加了一个 `write_sysreg_hcr()` 辅助函数，以提高代码的可读性和可维护性，并对错误描述进行了更具体的说明。

本周的讨论主要集中在补丁的具体实现和代码修改上，涉及到多个文件的变更，包括 Kconfig、硬中断处理、系统寄存器、CPU 错误处理等。参与者 D Scott Phillips 提出了这些更新，并在邮件中详细列出了代码的修改情况。总体来看，本周的讨论推动了补丁的进一步完善，为解决 AmpereOne 处理器的相关错误奠定了基础。

#### 📝 邮件列表

1. **[04-24 19:47]** [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>

---

### Thread 11: [PATCH 6.14 227/241] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 23 Apr 2025 16:44:51 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构中启用 FEAT_PMUv3p9 的 EL2 要求的补丁。该补丁的主要内容是添加一个新的初始化助手函数 `__init_el2_fgt2()`，用于配置细粒度陷阱控制寄存器 HDFGRTR2_EL2 和 HDFGWTR2_EL2，以便在 EL1 中访问 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1 寄存器。

在之前的讨论中，补丁的背景是为了支持 FEAT_PMUv3p9 特性，并确保在 EL2 中能够正确访问相关寄存器。补丁还更新了文档，明确了在 EL2 中访问 FEAT_FGT2 基于的寄存器所需的 SCR_EL3.FGTEn2 配置。

本周的新讨论中，Greg Kroah-Hartman 提出了该补丁的审查请求，并询问是否有任何异议。补丁得到了 Rob Herring 的测试和审核，表明其在功能上得到了认可。整体来看，该补丁旨在增强 arm64 架构的性能监控能力，并确保在特定条件下的寄存器访问不会导致陷阱。

#### 📝 邮件列表

1. **[04-23 16:44]** [PATCH 6.14 227/241] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---

### Thread 12: [PATCH 6.12 192/223] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 23 Apr 2025 16:44:24 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁，旨在启用 EL2 对 FEAT_PMUv3p9 的要求。补丁的核心内容是添加一个新的初始化助手函数 `__init_el2_fgt2()`，以配置细粒度陷阱控制寄存器 HDFGRTR2_EL2 和 HDFGWTR2_EL2，使得 EL1 中对 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1 寄存器的访问能够顺利进行。

在历史讨论中，并未提及具体的背景信息或先前的讨论内容，因此本周的新讨论成为了主要关注点。本周的邮件中，Greg Kroah-Hartman 提出了该补丁的审核请求，并询问是否有任何反对意见。补丁已获得 Rob Herring 的测试和审核确认，显示出其在功能上的有效性。

总结来说，本周的讨论主要集中在补丁的发布和审核上，补丁通过了测试，且没有收到反对意见，预计将会被合并到主线代码中。

#### 📝 邮件列表

1. **[04-23 16:44]** [PATCH 6.12 192/223] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---

## 📌 RFC

共 3 个 thread

---

### Thread 1: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1

**📧 邮件数**: 39 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 24 Apr 2025 15:13:07 +0100

#### 🤖 AI 总结

本邮件讨论主题为「通过 KVM 在 EL1 上运行 Qualcomm 的 Gunyah 客户端」，主要涉及将 Gunyah 超级管理程序与 KVM 集成的补丁系列。

1. **原始补丁/问题内容**：
   该补丁系列旨在将 Gunyah 超级管理程序的支持从独立驱动程序接口迁移到 KVM，以利用现有的 KVM 基础设施，减少内存管理、IRQ 等核心组件的重复工作。

2. **之前讨论要点**：
   之前的讨论集中在如何将 Gunyah 的功能与 KVM 结合，尤其是如何处理虚拟机的生命周期管理、内存分配和 IRQ 注入等。参与者提到，Gunyah 是一种 Type-1 超级管理程序，独立于任何高层操作系统内核。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Karim Manaouil 提出了多个补丁，增加了对 Gunyah 的支持，包括内存共享、虚拟 CPU 管理、IRQ 注入等功能。Oliver Upton 和 Trilok Soni 表达了对将 Gunyah 与 KVM 混合使用的担忧，认为 KVM 应该专注于自身的架构，而不是作为第三方超级管理程序的通用接口。最终，Karim 认可了这一观点，并表示此补丁对希望在 EL1 上运行 KVM 的用户仍有吸引力。

整体来看，讨论围绕如何在 KVM 中实现 Gunyah 的功能展开，同时也反映出对 KVM 作为一个独立虚拟化平台的重视。

#### 📝 邮件列表

1. **[04-24 15:13]** [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
2. **[04-24 15:13]** [RFC PATCH 01/34] KVM: Allow arch-specific vCPU allocation and freeing
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
3. **[04-24 15:13]** [RFC PATCH 02/34] KVM: irqfd: Add architecture hooks for irqfd allocation and initialization
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
4. **[04-24 15:13]** [RFC PATCH 03/34] KVM: irqfd: Allow KVM backends to override IRQ injection via set_irq callback
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
5. **[04-24 15:13]** [RFC PATCH 04/34] KVM: Add weak stubs for irqchip-related functions for Gunyah builds
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
6. **[04-24 15:13]** [RFC PATCH 05/34] KVM: Add KVM_SET_DTB_ADDRESS ioctl to pass guest DTB address from userspace
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
7. **[04-24 15:13]** [RFC PATCH 06/34] KVM: gunyah: Add initial Gunyah backend support
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
8. **[04-24 15:13]** [RFC PATCH 07/34] KVM: gunyah: Pin guest memory
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
9. **[04-24 15:13]** [RFC PATCH 08/34] docs: gunyah: Introduce Gunyah Hypervisor
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
10. **[04-24 15:13]** [RFC PATCH 09/34] dt-bindings: Add binding for gunyah hypervisor
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
11. **[04-24 15:13]** [RFC PATCH 10/34] gunyah: Common types and error codes for Gunyah hypercalls
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
12. **[04-24 15:13]** [RFC PATCH 11/34] gunyah: Add hypercalls to identify Gunyah
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
13. **[04-24 15:13]** [RFC PATCH 12/34] gunyah: Add hypervisor driver
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
14. **[04-24 15:13]** [RFC PATCH 13/34] gunyah: Add hypercalls to send and receive messages
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
15. **[04-24 15:13]** [RFC PATCH 14/34] gunyah: Add resource manager RPC core
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
16. **[04-24 15:13]** [RFC PATCH 15/34] gunyah: Add VM lifecycle RPC
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
17. **[04-24 15:13]** [RFC PATCH 16/34] gunyah: Add basic VM lifecycle management
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
18. **[04-24 15:13]** [RFC PATCH 17/34] gunyah: Translate gh_rm_hyp_resource into gunyah_resource
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
19. **[04-24 15:13]** [RFC PATCH 18/34] gunyah: Add resource tickets
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
20. **[04-24 15:13]** [RFC PATCH 19/34] gunyah: Add hypercalls for running a vCPU
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
21. **[04-24 15:13]** [RFC PATCH 20/34] gunyah: add proxy-scheduled vCPUs
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
22. **[04-24 15:13]** [RFC PATCH 21/34] gunyah: Add hypercalls for demand paging
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
23. **[04-24 15:13]** [RFC PATCH 22/34] gunyah: Add memory parcel RPC
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
24. **[04-24 15:13]** [RFC PATCH 23/34] gunyah: Add interfaces to map memory into guest address space
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
25. **[04-24 15:13]** [RFC PATCH 24/34] gunyah: Add platform ops on mem_lend/mem_reclaim
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
26. **[04-24 15:13]** [RFC PATCH 25/34] gunyah: Add Qualcomm Gunyah platform ops
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
27. **[04-24 15:13]** [RFC PATCH 26/34] gunyah: Share memory parcels
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
28. **[04-24 15:13]** [RFC PATCH 27/34] gunyah: Share guest VM dtb configuration to Gunyah
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
29. **[04-24 15:13]** [RFC PATCH 28/34] gunyah: Add RPC to enable demand paging
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
30. **[04-24 15:13]** [RFC PATCH 29/34] gunyah: Enable demand paging
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
31. **[04-24 15:13]** [RFC PATCH 30/34] gunyah: Add RPC to set VM boot context
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
32. **[04-24 15:13]** [RFC PATCH 31/34] gunyah: allow userspace to set boot cpu context
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
33. **[04-24 15:13]** [RFC PATCH 32/34] gunyah: Add hypercalls for sending doorbell
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
34. **[04-24 15:13]** [RFC PATCH 33/34] KVM: gunyah: Implement irqfd interface
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
35. **[04-24 15:13]** [RFC PATCH 34/34] KVM: gunyah: enable KVM for Gunyah
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
36. **[04-24 08:34]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
37. **[04-24 09:12]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Trilok Soni <quic_tsoni@quicinc.com>
38. **[04-24 17:43]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Karim Manaouil <karim.manaouil@linaro.org>
39. **[04-24 17:57]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC] ARM vGIC-ITS tables serialization when running protected VMs

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 14 Apr 2025 12:12:43 +0100

#### 🤖 AI 总结

本邮件线程讨论了在运行受保护虚拟机时，ARM vGIC-ITS（虚拟中断控制器）表的序列化问题。最初的补丁（patch）由Ilias Stamatis提出，旨在解决KVM的ARM虚拟中断翻译服务（ITS）接口在保存和恢复设备表时，因受保护虚拟机（如pKVM）无法访问来宾内存而引发的问题。

在历史讨论中，Marc Zyngier对该补丁表示反对，认为受保护虚拟机不应允许来宾内存的保存和恢复，并建议使用现有API共享页面对齐的内存。David Woodhouse则指出，GIC规范的重新定义可能会导致安全隐患，并强调应通过KVM将状态传递给用户空间以进行迁移。

在本周的新讨论中，David Woodhouse再次对补丁提出质疑，认为将GIC放在IOMMU后以实现页面粒度的访问控制是更合理的方案。Marc Zyngier则反驳称，Linux在机密基础设施下已成功实现了页面大小数据的暴露，认为这种方法是可行的。双方对如何处理GIC架构和KVM API的复杂性展开了激烈的辩论，未能达成共识。整体来看，讨论集中在如何安全有效地管理受保护虚拟机的中断表及其内存访问问题上。

#### 📝 邮件列表

1. **[04-14 12:12]** [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Ilias Stamatis <ilstam@amazon.com>
2. **[04-15 09:35]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-15 10:44]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
4. **[04-22 11:47]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
5. **[04-27 17:37]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-27 17:43]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected VMs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 13:40:56 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 MTE（Memory Tagging Extension）功能的支持问题，主要集中在如何正确处理 MTE_frac 字段。

**原始 patch/问题的内容**：
Ben Horgan 提出的补丁系列旨在解决当前 KVM 隐藏 ID_AA64PFR1_EL1.MTE_frac 字段的问题。该字段在特定条件下（ID_AA64PFR1_EL1.MTE==2）可以指示 MTE_ASYNC 是否被支持。若主机支持 MTE 但不支持 MTE_ASYNC，虚拟机可能错误地认为 MTE_ASYNC 被支持。补丁的目的是修复这一问题，确保虚拟机能够正确识别其所支持的功能。

**之前的讨论要点**：
在历史讨论中，Horgan 强调了 MTE_frac 的重要性，并指出如果不根据 MTE 能力条件性地屏蔽 MTE_frac，虚拟机将始终看到该字段为 0，这可能导致错误的功能广告。补丁的核心在于根据主机的实际能力向虚拟机和用户空间暴露正确的 MTE_frac 值。

**本周的新讨论、进展或结论**：
在本周的讨论中，Marc Zyngier 对补丁提出了质疑，认为不应无条件地将硬件支持的信息传播给虚拟机，特别是在 MTE_frac 的未来演变尚不明确的情况下。他建议应将修复限制在特定的情况，而不是盲目覆盖虚拟机对硬件能力的视图。此讨论表明，尽管补丁的初衷是修复问题，但在实施时需要更加谨慎，以避免潜在的后续问题。

#### 📝 邮件列表

1. **[04-14 13:40]** [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[04-14 13:40]** [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[04-27 18:24]** Re: [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.15, round #2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 18 Apr 2025 14:01:58 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的一个重要修复补丁，该补丁旨在解决 PV MIDR 基础设施引起的启动失败问题。历史讨论中，Oliver Upton 提到该补丁经过 Catalin 的审核，并请求在工作周结束前进行合并，强调了其紧急性。

在本周的新讨论中，Paolo Bonzini 对 Oliver 的请求进行了确认，表示已经完成了相关操作，并感谢了对方的耐心。这表明该补丁已成功合并，解决了之前提到的启动问题。

总结而言，此次讨论围绕一个关键的修复补丁展开，历史讨论提供了背景信息，而本周的进展则确认了补丁的合并，标志着问题的解决。

#### 📝 邮件列表

1. **[04-18 14:01]** [GIT PULL] KVM/arm64 fixes for 6.15, round #2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[04-24 19:36]** Re: [GIT PULL] KVM/arm64 fixes for 6.15, round #2
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 14 个 thread

---

### Thread 1: Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.14-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 09:18:09 +0200

#### 🤖 AI 总结

本邮件讨论的主题是补丁“arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9”，该补丁已被添加到6.14-stable树中。补丁的主要内容是为FEAT_PMUv3p9特性添加EL2要求，具体包括对PMICNTR_EL0、PMICFILTR_EL0和PMUACR_EL1寄存器的访问需要通过FEAT_FGT2的细粒度陷阱控制寄存器进行配置，以避免陷入EL2。

在之前的讨论中，补丁的必要性和实现细节已被提及，主要集中在如何正确初始化相关的细粒度陷阱控制寄存器，以确保在EL1下能够顺利访问这些寄存器。

本周的新进展是，补丁已正式添加到稳定树中，邮件中指出了补丁的文件名和存放位置，并邀请其他开发者如果认为不应添加该补丁，可以联系稳定邮件列表。此补丁的添加标志着对ARM架构在性能监控方面的支持进一步增强，确保了在特定条件下的寄存器访问的正确性。

#### 📝 邮件列表

1. **[04-22 09:18]** Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.14-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 2: Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.12-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 09:16:59 +0200

#### 🤖 AI 总结

本邮件讨论的主题是补丁“arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9”，该补丁已被添加到6.12稳定树中。补丁的主要内容是为FEAT_PMUv3p9特性添加EL2的要求，具体包括通过新辅助函数`__init_el2_fgt2()`初始化细粒度陷阱控制寄存器，以便允许从EL1访问PMICNTR_EL0、PMICFILTR_EL0和PMUACR_EL1寄存器。

在历史讨论中，补丁的背景信息指出，FEAT_PMUv3p9寄存器的访问需要适当的EL2细粒度陷阱配置，否则会导致陷入EL2。补丁还更新了文档，明确了在EL2中访问FEAT_FGT2相关寄存器的要求。

本周的新讨论中，参与者Greg Kroah-Hartman通知大家该补丁已成功添加到稳定树，并提供了补丁的链接和文件名。如果有任何人认为该补丁不应被添加到稳定树，可以联系稳定邮件列表。此次讨论没有其他新的技术问题或争议，主要是对补丁添加的确认。

#### 📝 邮件列表

1. **[04-22 09:16]** Patch "arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9" has been added to the 6.12-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 3: Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.ZEN" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:55 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁“KVM: arm64: Remove VHE host restore of CPACR_EL1.ZEN”添加到6.1-stable树的通知。

该补丁的主要内容是移除在KVM的VHE模式下，主机内核对CPACR_EL1.ZEN配置的保存和恢复逻辑。由于VHE hyp代码在返回主机时会无条件地将CPTR_EL2.ZEN配置为0b01，因此主机内核不再需要保存和恢复EL0 SVE的状态，这一逻辑显得多余。

在历史讨论中，补丁的提出者Mark Rutland解释了当前的逻辑是冗余的，并指出主机内核已经能够安全地保存和恢复状态，而无需进行陷阱处理。补丁得到了多位开发者的审核和确认。

在本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功添加到6.1-stable树，并提供了补丁文件的链接。如果有任何人认为该补丁不应被添加到稳定树，欢迎联系稳定邮件列表。这一进展表明补丁已经通过审核并正式纳入了内核版本中。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.ZEN" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 4: Patch "KVM: arm64: Unconditionally save+flush host FPSIMD/SVE/SME state" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:55 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁“KVM: arm64: Unconditionally save+flush host FPSIMD/SVE/SME state”添加到6.1稳定树的通知。

补丁的主要内容是解决KVM在处理ARM64架构时，主机的FPSIMD/SVE/SME状态的保存和刷新问题。之前的实现存在多个问题，例如主机SVE状态可能因配置不一致而被意外丢弃，导致QEMU崩溃。此外，主机的FPMR值在某些情况下未能正确保存，可能导致内存中的过时值。为了解决这些问题，补丁通过在加载虚拟CPU时主动保存和刷新主机的FPSIMD/SVE/SME状态，避免了KVM需要保存这些状态的需求。

在历史讨论中，补丁的背景提到，早在v5.17版本就存在对TIF_SVE的错误假设，导致了不必要的状态丢失。补丁的设计旨在修复这些历史遗留问题，并建议在所有稳定树中进行回溯。

本周的新进展是，Greg Kroah-Hartman确认已将该补丁成功添加到6.1稳定树，并提供了补丁的相关链接。如果有任何人认为该补丁不应被添加，请联系稳定邮件列表。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Unconditionally save+flush host FPSIMD/SVE/SME state" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 5: Patch "KVM: arm64: Calculate cptr_el2 traps on activating traps" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于补丁“KVM: arm64: Calculate cptr_el2 traps on activating traps”的更新，该补丁已被添加到6.1-stable树中。

补丁的主要内容是，在激活陷阱时从头计算cptr_el2的值，避免了在每个虚拟CPU结构中存储cptr_el2的需求。这一改动还确保了某些陷阱（例如，来宾是否拥有浮点寄存器）在每次虚拟CPU运行时都能被正确设置。

在历史讨论中，补丁的提出者Fuad Tabba指出，类似于VHE（虚拟化扩展），这种方法能简化KVM的实现，并解决了之前在处理浮点寄存器所有权时的一些问题。补丁的修复也得到了多位开发者的支持和签名。

在本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功合并到6.1-stable树中，并提供了补丁的链接和文件名。如果有任何人认为该补丁不应被添加到稳定树中，可以联系相关邮箱进行反馈。整体来看，该补丁的合并标志着对KVM在arm64架构下的进一步优化和完善。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Calculate cptr_el2 traps on activating traps" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 6: Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.SMEN" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁“KVM: arm64: Remove VHE host restore of CPACR_EL1.SMEN”添加到6.1稳定树的通知。

该补丁的主要内容是移除在VHE模式下，KVM主机对CPACR_EL1.SMEN的保存和恢复逻辑。历史上，这一逻辑是为了防止在运行vCPU时，主机的SME状态被破坏。然而，随着内核对FPSIMD/SVE/SME状态的处理方式的改进，这一逻辑变得多余且冗长。补丁的提出者Mark Rutland指出，现有的内核能够安全地保存和恢复状态，而无需再进行此类操作。

在之前的讨论中，补丁的背景涉及到多个相关提交，特别是861262ab86270206和375110ab51dec5dc，这些提交分别引入了对SME状态的处理和修复了相关的安全问题。

本周的进展是，Greg Kroah-Hartman确认已将该补丁添加到6.1稳定树，并提供了补丁的链接和文件名。如果有任何人认为该补丁不应被添加到稳定树，可以联系稳定邮件列表进行反馈。整体来看，此补丁的添加标志着对KVM在VHE模式下的状态管理的进一步优化。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.SMEN" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 7: Patch "KVM: arm64: Remove host FPSIMD saving for non-protected KVM" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本周讨论的主题是关于补丁“KVM: arm64: Remove host FPSIMD saving for non-protected KVM”，该补丁已被添加到6.1-stable树中。补丁的主要内容是移除在非保护模式下，KVM保存主机FPSIMD/SVE/SME状态的代码，因为在这种模式下主机会主动保存其自身的状态，且相关代码未被使用。对于保护模式，仍需保存和恢复主机的FPSIMD/SVE状态，以避免泄露来宾状态。

在历史讨论中，补丁的作者Mark Rutland指出，现有的代码结构中存在冗余，因此提出了删除未使用的代码和数据结构的建议。补丁得到了多位开发者的审查和认可。

本周的新进展是，补丁已正式添加到稳定树中，开发者Greg Kroah-Hartman通知了相关人员，并提供了补丁的链接。如果有人认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。整体来看，此次补丁的合并标志着KVM在处理FPSIMD状态方面的代码优化，提升了系统的效率和安全性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Remove host FPSIMD saving for non-protected KVM" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 8: Patch "KVM: arm64: Refactor exit handlers" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于将补丁“KVM: arm64: Refactor exit handlers”添加到6.1稳定树的通知。该补丁的主要内容是重构ARM64架构下KVM的退出处理程序，以消除头文件对C文件的依赖，从而避免编译时的警告。补丁确保功能不变，主要是改善代码结构。

在历史讨论中，补丁由Mark Rutland提出，并得到了多位开发者的审查和测试，包括Mark Brown和Will Deacon等。补丁的目的是解决在使用共享逻辑时出现的编译警告问题。

本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功添加到6.1稳定树，并提供了补丁文件的链接。他还提醒如果有人认为该补丁不应被添加到稳定树，可以联系相关邮箱。至此，该补丁的添加过程顺利完成，没有额外的反对意见或讨论。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Refactor exit handlers" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 9: Patch "KVM: arm64: Mark some header functions as inline" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于补丁“KVM: arm64: Mark some header functions as inline”的更新，该补丁已被添加到6.1-stable树中。补丁的主要内容是将一些头文件中的静态函数标记为内联，以避免在未使用时引发编译器警告。这些函数包括`kvm_hyp_handle_dabt_low`、`kvm_hyp_handle_cp15_32`等，标记为内联后不会影响功能。

在历史讨论中，补丁的作者Mark Rutland详细说明了为何需要此更改，指出在某些情况下，未使用的静态函数会导致编译器产生警告。补丁还对函数的别名使用进行了调整，以符合内核的其他部分风格。

本周的更新由Greg Kroah-Hartman发送，确认该补丁已成功添加到6.1-stable树中，并提供了补丁的链接。如果有任何人认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。整体来看，此补丁旨在提高代码质量，减少不必要的编译警告。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Mark some header functions as inline" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 10: Patch "KVM: arm64: Eagerly switch ZCR_EL{1,2}" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件主题为“Patch 'KVM: arm64: Eagerly switch ZCR_EL{1,2}' 已添加至 6.1-stable 树”，主要讨论了一个针对 KVM 的补丁。

1. **原始补丁内容**：该补丁的标题为“KVM: arm64: Eagerly switch ZCR_EL{1,2}”，其目的是在 KVM 的 guest 和 host 之间切换时，主动更新 ZCR_EL1 和 ZCR_EL2 寄存器，以避免在处理 guest 状态时出现的 FPSIMD/SVE 状态保存失败的问题。

2. **之前讨论要点**：在历史讨论中，补丁的背景主要涉及在非保护模式下，guest 的 FPSIMD/SVE 状态可能与 host 的状态不一致，导致在切换时可能出现 SIGKILL 信号。补丁通过在 guest 和 host 之间的切换时主动更新 ZCR 寄存器，简化了处理逻辑，避免了对 host SVE 使用的陷阱。

3. **本周的新讨论与进展**：本周，Greg Kroah-Hartman 通知大家该补丁已成功添加至 6.1-stable 树，并提供了补丁文件的链接。他还提醒如果有人认为该补丁不应被添加，可以联系稳定邮件列表。

总体而言，该补丁旨在提升 KVM 在 ARM64 架构下的性能和稳定性，确保在 guest 和 host 切换时的状态一致性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Eagerly switch ZCR_EL{1,2}" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 11: Patch "KVM: arm64: Discard any SVE state when entering KVM guests" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:54 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于补丁“KVM: arm64: Discard any SVE state when entering KVM guests”的更新，该补丁已被添加到6.1-stable树中。

1. **原始补丁内容**：该补丁旨在处理KVM在进入虚拟机时丢弃任何SVE（Scalable Vector Extension）状态。自从之前的提交8383741ab2e773a99以来，KVM不再跟踪主机的SVE状态，而是依赖于在执行系统调用时禁用SVE。补丁通过在准备运行虚拟机时清除TIF_SVE标志并将存储的任务状态转换为FPSIMD格式来解决这一问题。

2. **之前讨论要点**：虽然邮件中没有详细记录之前的讨论，但可以推测，此补丁是对KVM在处理SVE状态时的一种优化，旨在提高性能并避免未来可能出现的状态管理问题。

3. **本周的新讨论与进展**：本周的更新由Greg Kroah-Hartman发送，确认该补丁已成功添加到6.1-stable树中，并提供了补丁的文件名和存放路径。邮件中还提到，如果有人认为该补丁不应被添加到稳定树，可以联系相应的邮箱进行反馈。

总之，此补丁的添加是对KVM在处理SVE状态时的一项重要改进，旨在提高系统的性能和稳定性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "KVM: arm64: Discard any SVE state when entering KVM guests" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 12: Patch "arm64/fpsimd: Track the saved FPSIMD state type separately to TIF_SVE" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:53 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁的更新，标题为“arm64/fpsimd: Track the saved FPSIMD state type separately to TIF_SVE”，该补丁已被添加到6.1-stable树中。

补丁的主要内容是引入一个新的枚举类型，用于在保存浮点寄存器状态时，明确指示当前使用的状态格式（FPSIMD或SVE）。这样做的目的是优化系统调用的处理，尤其是在SVE情况下，当前的实现依赖于TIF_SVE标志，限制了优化的可能性。补丁在`thread_struct`和KVM客体状态中添加了一个新的字段，以跟踪当前的浮点状态类型。

在之前的讨论中，补丁得到了多个开发者的审查和认可，包括Catalin Marinas和Marc Zyngier等人，确保了其合理性和必要性。

本周的新进展是，Greg Kroah-Hartman通知大家该补丁已成功添加到6.1-stable树中，并提供了补丁的具体文件名和存放位置。他还邀请其他开发者如果认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。整体来看，该补丁的添加标志着对ARM64架构浮点状态管理的进一步完善。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "arm64/fpsimd: Track the saved FPSIMD state type separately to TIF_SVE" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 13: Patch "arm64/fpsimd: Stop using TIF_SVE to manage register saving in KVM" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:53 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch）“arm64/fpsimd: Stop using TIF_SVE to manage register saving in KVM”，该补丁已被添加到6.1-stable树中。补丁的主要内容是停止在KVM中使用TIF_SVE来管理寄存器的保存，转而依赖于to_save来确保保存正确的数据。这一更改旨在简化KVM代码，并优化常规任务的处理，且不会对功能或性能产生影响。

在历史讨论中，补丁的作者Mark Brown和其他几位开发者（如Catalin Marinas和Marc Zyngier）进行了审查，确认了补丁的有效性和必要性。补丁的背景是，之前的实现中，KVM代码需要手动管理TIF_SVE标志，而现在通过明确告知主机FP代码需要保存的寄存器状态，可以简化这一过程。

在本周的新讨论中，Greg Kroah-Hartman通知大家该补丁已成功添加到稳定树中，并提供了补丁的链接和文件名。如果有任何人认为该补丁不应被添加到稳定树中，可以联系稳定邮件列表。没有其他新的争论或问题提出，表明该补丁的接受过程顺利。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "arm64/fpsimd: Stop using TIF_SVE to manage register saving in KVM" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 14: Patch "arm64/fpsimd: Have KVM explicitly say which FP registers to save" has been added to the 6.1-stable tree

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 22 Apr 2025 08:43:53 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁的更新，标题为“arm64/fpsimd: Have KVM explicitly say which FP registers to save”，该补丁已被添加到6.1-stable树中。

该补丁的主要内容是为了优化KVM在上下文切换时对FP（浮点）寄存器的保存和恢复过程。当前，KVM依赖于主机的FPSIMD代码来保存寄存器状态，这种方式复杂且不够直接。补丁提议让KVM在绑定到CPU时明确指定需要保存的寄存器状态，引入了一个新的状态标识符FP_STATE_CURRENT，以便在正常任务绑定时使用。

在之前的讨论中，补丁的设计意图和实现细节得到了确认，确保在未来的调试中能够更清晰地跟踪寄存器状态的保存需求。

本周的新进展是该补丁已正式被纳入6.1-stable树，参与者Greg Kroah-Hartman通知了邮件列表，表示如果有任何人认为该补丁不应被添加，可以联系稳定性维护团队。此补丁的添加标志着对KVM寄存器管理的进一步优化，旨在提高系统的性能和稳定性。

#### 📝 邮件列表

1. **[04-22 08:43]** Patch "arm64/fpsimd: Have KVM explicitly say which FP registers to save" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

